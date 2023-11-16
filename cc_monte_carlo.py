def monte_carlo(T, p_star, u, d, S_0, K, n):
    S = S_0
    sum_C = 0
    for i in range(0,n):
        S_i = S_0
        for j in range(1,T + 1):
            if random.random() > p_star:
                S_i *= u
            else:
                S_i *= d
        C_i = S_i - K
        # print(C_i)
        sum_C += C_i

    return sum_C / n

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

    print("n = 100:", avg_100)
    print("n = 1000:", avg_1000)
    print("n = 10000:", avg_10000)

calc_ans()
