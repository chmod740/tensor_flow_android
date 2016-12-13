import tensorflow as tf
import numpy as np


def tf_mul(fft_final):
    #第一次tf矩阵乘法
    matrixl = tf.constant(fft_final)
    x_data = np.float64(np.random.rand(161, 100))  # 随机输入
    matrix2 = tf.constant(x_data)
    product = tf.matmul(matrixl, matrix2)
    sess = tf.Session()
    result = sess.run(product)

    #第二次tf矩阵乘法
    matrixl = tf.constant(result)
    x_data = np.float64(np.random.rand(100, 100))  # 随机输入
    matrix2 = tf.constant(x_data)
    product = tf.matmul(matrixl, matrix2)
    sess = tf.Session()
    result = sess.run(product)

    #第三次tf矩阵乘法
    matrixl = tf.constant(result)
    x_data = np.float64(np.random.rand(100, 161))  # 随机输入
    matrix2 = tf.constant(x_data)
    product = tf.matmul(matrixl, matrix2)
    sess = tf.Session()
    result = sess.run(product)
    sess.close()

    #ifft&元素转实数
    ifft_final = np.fft.ifft(result)
    num=0
    temp = ifft_final.tolist()
    temp = temp[0]
    for i in temp:
        temp[num] = np.sqrt(i.real * i.real + i.imag * i.imag)
        num = num + 1
    ifft_final = np.mat(temp)
    print(ifft_final.shape)
    print(ifft_final)
    return ifft_final
