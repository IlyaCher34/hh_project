a
    X�d=  �                   @   sD   d dl Zd
eed�dd�Zede� � �� ed�dd	�Zee� dS )�    N�   )�number�returnc                 C   s*   d}|d7 }t j�dd�}| |krq&q|S )u�   Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    r   r   �e   )�np�random�randint)r   �countZpredict_number� r
   �$/Users/ilacernikov/vscode/game_v2.py�random_predict   s    	r   u%   Количество попыток: )r   c                 C   s\   g }t j�d� t jjdddd�}|D ]}|�| |�� q&tt �|��}td|� d�� |S )u.  За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    r   r   i�  )�sizeuN   Ваш алгоритм угадывает число в среднем за: u    попыток)r   r   �seedr   �append�int�mean�print)r   Zcount_lsZrandom_arrayr   �scorer
   r
   r   �
score_game   s    
r   )r   )�numpyr   r   r   r   r   r
   r
   r
   r   �<module>   s   