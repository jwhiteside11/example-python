

def monte_carlo(T, p_star, u, d, S_0, K, n):
    sum_C = 0
    for i in range(n):
        S_i = S_0
        for j in range(T):
            if random.random() < p_star:
                S_i *= u
            else:
                S_i *= d
        C_i = S_i - K
        # print(C_i)
        sum_C += C_i

    return sum_C / n


f_memo = [1, 1]


def f(n):
    if n < len(f_memo):
        return f_memo[n]

    a = f_memo[0]

    for i in range(1, n+1):
        if i < len(f_memo):
            a = f_memo[i]
        else:
            a *= i
            f_memo.append(a)

    return a


def nCk(n, k):
    return f(n) / (f(k) * f(n-k))


def bsm(T, p_star, u, d, S_0, K):
    sum_term = 0

    for k in range(T+1):
        tCk = nCk(T, k)
        prob = (p_star ** k) * ((1 - p_star) ** (T - k))
        updown = (u ** k) * (d ** (T - k)) * S_0 - K
        # print(tCk, prob, updown)
        sum_term += tCk * prob * updown

    return sum_term

def calc_ans():
    T_ = 10
    r_ = 0.05
    u_ = 1.15
    d_ = 1.01
    S_0_ = 50
    K_ = 70

    p_star = (1 + r_ - d_) / (u_ - d_)
    print("p* =", p_star)

    avg_100 = monte_carlo(T_, p_star, u_, d_, S_0_, K_, 100)
    avg_1000 = monte_carlo(T_, p_star, u_, d_, S_0_, K_, 1000)
    avg_10000 = monte_carlo(T_, p_star, u_, d_, S_0_, K_, 10000)

    ans_bsm = bsm(T_, p_star, u_, d_, S_0_, K_)

    print("Monte-Carlo simulation:")
    print("n = 100:", avg_100)
    print("n = 1000:", avg_1000)
    print("n = 10000:", avg_10000)
    print("Black-Scholes-Merton:", ans_bsm)


calc_ans()
