{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3d942f4c-e874-473e-aaca-f44883baca21",
   "metadata": {},
   "source": [
    "##                                      Basics of Probability"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eab0f5f5-9906-4584-b8ca-5ac128fa3680",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce73ac06-a51a-4dfb-ae48-7f9bc7cfa0a0",
   "metadata": {},
   "source": [
    "# 1.a Tossing a coin 10,000 times and calculating the experimental probability of heads and tails"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8f234150-d7a3-45d4-9d76-6c7407269d5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Experimental Probability of Heads: 0.4969\n",
      "Experimental Probability of Tails: 0.5031\n"
     ]
    }
   ],
   "source": [
    "tosses = 10000\n",
    "heads = 0\n",
    "tails = 0\n",
    "for _ in range(tosses):\n",
    "    result = random.choice(['H', 'T'])\n",
    "    if result == 'H':\n",
    "        heads += 1\n",
    "    else:\n",
    "        tails += 1\n",
    "prob_heads = heads / tosses\n",
    "prob_tails = tails / tosses\n",
    "\n",
    "print(f\"Experimental Probability of Heads: {prob_heads}\")\n",
    "print(f\"Experimental Probability of Tails: {prob_tails}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0eadf18-1401-40c7-8ef5-6cee5424b243",
   "metadata": {},
   "source": [
    "# 1.b Rolling two dice and computing the probability of getting a sum of 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f3990f0f-b977-4fcf-b5ce-8798fe22c7b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Two Dice Simulation\n",
      "Number of times sum is 7: 1645\n",
      "Probability of getting sum 7: 0.1645\n"
     ]
    }
   ],
   "source": [
    "trials = 10000\n",
    "sum_seven = 0\n",
    "\n",
    "for _ in range(trials):\n",
    "    die1 = random.randint(1, 6)\n",
    "    die2 = random.randint(1, 6)\n",
    "    if die1 + die2 == 7:\n",
    "        sum_seven += 1\n",
    "\n",
    "prob_sum_seven = sum_seven / trials\n",
    "print(\"\\nTwo Dice Simulation\")\n",
    "print(\"Number of times sum is 7:\", sum_seven)\n",
    "print(\"Probability of getting sum 7:\", prob_sum_seven)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36fa9fa2-b463-4cb0-a0d8-56c85ac44456",
   "metadata": {},
   "source": [
    "# 2 function to estimate the probability of getting at least one \"6\" in 10 rolls of a fair die."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d6a502e5-93af-46b6-bb13-429d0fc8fff6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def probability_at_least_one_six(trials=10000):\n",
    "    success = 0\n",
    "    for i in range(trials):\n",
    "        found_six = False\n",
    "        for i in range(10):\n",
    "            if random.randint(1, 6) == 6:\n",
    "                found_six = True\n",
    "                break\n",
    "        if found_six:\n",
    "            success += 1\n",
    "            return success / trials\n",
    "            result = probability_at_least_one_six()\n",
    "                        \n",
    "            print(\"Probability of getting at least one 6 in 10 rolls:\", result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f953531f-fcc5-4a54-8258-125d66232a7e",
   "metadata": {},
   "source": [
    "# Conditional Probability and Bayes' Theorem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "359c53ec-c392-4b48-af80-bf5f6cebe4fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "67ba371c-72de-4e79-8cd5-c642039a33af",
   "metadata": {},
   "outputs": [],
   "source": [
    "bag = ['Red'] * 5 + ['Green'] * 7 + ['Blue'] * 8\n",
    "trials = 1000\n",
    "\n",
    "previous_blue = 0\n",
    "red_given_blue = 0\n",
    "\n",
    "count_red = 0\n",
    "count_blue = 0\n",
    "blue_given_red = 0\n",
    "\n",
    "previous_ball = None\n",
    "\n",
    "for _ in range(trials):\n",
    "    current_ball = random.choice(bag)\n",
    "\n",
    "    # Count total reds and blues\n",
    "    if current_ball == 'Red':\n",
    "        count_red += 1\n",
    "    if current_ball == 'Blue':\n",
    "        count_blue += 1\n",
    "\n",
    "    # Conditional counting\n",
    "    if previous_ball == 'Blue':\n",
    "        previous_blue += 1\n",
    "        if current_ball == 'Red':\n",
    "            red_given_blue += 1\n",
    "\n",
    "    if previous_ball == 'Red' and current_ball == 'Blue':\n",
    "        blue_given_red += 1\n",
    "\n",
    "    previous_ball = current_ball"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "4bbaf333-4eac-4e42-9c9f-f69f723c7442",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P(Red | Previous was Blue): 0.2631578947368421\n"
     ]
    }
   ],
   "source": [
    "rob_red_given_blue = red_given_blue / previous_blue\n",
    "print(\"P(Red | Previous was Blue):\", rob_red_given_blue)  # Changed variable name to match the one defined above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e1762cb8-a49b-4a00-9f71-900e901bf713",
   "metadata": {},
   "outputs": [],
   "source": [
    "P_red = count_red / trials\n",
    "P_blue = count_blue / trials\n",
    "P_blue_given_red = blue_given_red / count_red"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b07596c0-909a-4a34-98ae-8b9ae7870ab3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bayes Theorem Result: 0.24473684210526314\n",
      "\n",
      "Verification:\n",
      "Simulation P(Red | Blue): 0\n",
      "Bayes Theorem P(Red | Blue): 0.24473684210526314\n"
     ]
    }
   ],
   "source": [
    "prob_red_given_blue = 0  \n",
    "bayes_result = (P_blue_given_red * P_red) / P_blue\n",
    "print(\"Bayes Theorem Result:\", bayes_result)\n",
    "print(\"\\nVerification:\")\n",
    "print(\"Simulation P(Red | Blue):\", prob_red_given_blue)\n",
    "print(\"Bayes Theorem P(Red | Blue):\", bayes_result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "919416ae-c724-4653-9780-b1b894600b97",
   "metadata": {},
   "source": [
    "# Random Variables and Discrete Probability"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7fae110c-6c34-4e4b-ba84-decf12f84ff6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "cbec5069-43bd-4305-a9e4-2bc3bf537ad2",
   "metadata": {},
   "outputs": [],
   "source": [
    "values = [1, 2, 3]\n",
    "probabilities = [0.25, 0.35, 0.4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "4ef17f8d-255a-4b00-8760-ee8753ae3f82",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample = np.random.choice(values, size=1000, p=probabilities)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f82f0563-f723-4b3b-9b96-dac4bfe9e71f",
   "metadata": {},
   "source": [
    "# Computing the empirical mean, variance, and standard deviation of the sample"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "29d56364-4f04-4d12-80ab-80180eb06a6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empirical Mean: 2.136\n",
      "Empirical Variance: 0.6275040000000002\n",
      "Empirical Standard Deviation: 0.7921515006613319\n"
     ]
    }
   ],
   "source": [
    "mean = np.mean(sample)\n",
    "variance = np.var(sample)\n",
    "std_dev = np.std(sample)\n",
    "print(\"Empirical Mean:\", mean)\n",
    "print(\"Empirical Variance:\", variance)\n",
    "print(\"Empirical Standard Deviation:\", std_dev)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f92c855-051d-4449-880d-82ee4830e84d",
   "metadata": {},
   "source": [
    "# Continuous Random Variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "2ac4d1d7-c3b6-4747-9130-7c4d45bd6b5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "mean = 5\n",
    "samples = np.random.exponential(scale=mean, size=2000)\n",
    "\n",
    "plt.figure()\n",
    "plt.hist(samples, bins=30, density=True, alpha=0.5)\n",
    "x = np.linspace(0, max(samples), 1000)\n",
    "pdf = (1/mean) * np.exp(-x/mean)\n",
    "\n",
    "plt.plot(x, pdf)\n",
    "\n",
    "plt.xlabel(\"Value\")\n",
    "plt.ylabel(\"Density\")\n",
    "plt.title(\"Exponential Distribution (Mean = 5)\")\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8fe5eb4c-1a0f-43ad-801d-15b76c9ed0ce",
   "metadata": {},
   "source": [
    "# Central Limit Theorem\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "f3822bd0-d6d4-4054-b61a-60f7f01a92a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "9a0c8463-b3ce-4c85-90e4-cabf410cb389",
   "metadata": {},
   "outputs": [],
   "source": [
    "uniform_data = np.random.uniform(0, 1, 10000)\n",
    "sample_means = []\n",
    "\n",
    "for i in range(1000):\n",
    "    sample = np.random.choice(uniform_data, size=30)\n",
    "    sample_means.append(np.mean(sample))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "facf0b0d-2d8b-409a-957c-cc3dcba5d99f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjcAAAHFCAYAAAAOmtghAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAw5ElEQVR4nO3deXRUVb728acgZGBIkCkJEEIAh8goYaGAyGgQlFFbrtiEWVhoC0S8TYgyOUREuYDNYAskskSMIHDt7qhEQQiCyhBsu+GqzZAwJGISSZAhQHLeP1ip1zIBU0Ulldp8P2vVWtSufc75nZ1APex9TpXNsixLAAAAhqjm6QIAAADciXADAACMQrgBAABGIdwAAACjEG4AAIBRCDcAAMAohBsAAGAUwg0AADAK4QYAABiFcANUAXPmzJHNZlNOTk6Zr7dp00Y9e/Z0ad+jR49W8+bNHdry8vL0X//1X2rUqJFsNpuGDBni0r4rS8+ePWWz2WSz2VStWjXVqVNHrVq10h/+8Adt2LBBxcXFpbZp3ry5Ro8e7dRxdu3apTlz5ujMmTNObffbY33++eey2WzasGGDU/u5nvPnz2vOnDn6/PPPS72WlJQkm82mY8eOue14gDfz8XQBACrW888/rylTpji0vfDCC9q0aZNWr16tli1bql69eh6qrvxatGihtWvXSpLOnTuno0ePavPmzfrDH/6g7t27629/+5uCgoLs/Tdt2qTAwECnjrFr1y7NnTtXo0ePVt26dcu9nSvHctb58+c1d+5cSSoVdB988EHt3r1boaGhFVoD4C0IN4DhWrZsWartX//6l1q2bKnHH3/cLcewLEsXL15UQECAW/ZXloCAAN1zzz0ObePHj1diYqLGjh2rJ554QsnJyfbX7rrrrgqrpcSFCxcUEBBQKce6noYNG6phw4YerQGoSliWArxQybLHunXrFB8fr8aNGyswMFB9+/bVd99959D318tSx44dk81m06effqpDhw7Zl3pKljry8vI0efJkNWnSRL6+vmrRooXi4+NVWFjosE+bzaannnpKK1asUGRkpPz8/PT222/bl0e2bt2qCRMmqH79+goMDFRMTIzOnTun7OxsPfroo6pbt65CQ0M1ffp0Xb58+YbGYsyYMRowYIDWr1+vjIwMe/tvl4qKi4v14osv6vbbb1dAQIDq1q2rdu3aafHi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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAioAAAHFCAYAAADcytJ5AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA7R0lEQVR4nO3deVRV9f7/8dcBBEQGBWdFMM0R5zSncp4z0yyzmzlnV68383pvmuVQP0O0zNS0GTWHUhPzZjnllKU5m5ZXcyaHNE1QLAr4/P5ocb4eAWU4sDfyfKx11vLs/dl7v8+HfeDlZ08OY4wRAACADXlYXQAAAEBGCCoAAMC2CCoAAMC2CCoAAMC2CCoAAMC2CCoAAMC2CCoAAMC2CCoAAMC2CCoAAMC2CCq4rblz58rhcDhfvr6+Kl26tFq1aqXIyEhduHAhzTITJkyQw+HI0nauX7+uCRMmaNOmTVlaLr1thYeH64EHHsjSem5n0aJFmj59errzHA6HJkyY4NbtuduXX36pe+65R0WKFJHD4dCKFSsybBsbG6uhQ4eqSpUqKly4sIKDg1WrVi0NHjxYsbGxeVd0NqTurydPnnTL+k6ePOnc9zP6GQ8YMMDZ5k7w559/qlq1apo8ebLVpaRr/fr1ateuncqWLSsfHx+VLFlSrVu31ueff55h+yZNmsjPz0/FixdXv3790vze+vLLL+Xv768zZ87kxUdAFhBUkGnR0dHatm2b1q1bpzfffFN169ZVVFSUqlevrvXr17u0HTRokLZt25al9V+/fl0TJ07MclDJzray41ZBZdu2bRo0aFCu15Bdxhg9+uijKlSokFauXKlt27apRYsW6bb96aefVL9+fa1bt04jR47U559/rg8++EC9e/fWzp07dfz48Tyu3h4CAgI0d+5cpaSkuEy/du2ali5dqsDAQIsqc7/Zs2fr119/1fDhw60uJV2XLl1SzZo19frrr2vt2rV6++23VahQIXXp0kULFixwabt582Z16tRJpUqV0qeffqo33nhD69evV5s2bZSYmOhs16ZNGzVq1EjPP/98Xn8c3I4BbiM6OtpIMjt37kwz79SpUyY0NNQEBASY8+fP52g7Fy9eNJLM+PHjM9U+ISEhw3lhYWGmS5cuOarnZl26dDFhYWFuXWde+emnn4wkExUVddu248aNM5LM8ePH052fnJzs7vLcKnV/PXHihFvWd+LECSPJDBo0yEgya9eudZn/3nvvmcKFC5snnnjC3Am/Uv/8809Trlw5M3r0aKtLyZI//vjDlCtXztx3330u0xs2bGhq1Khh/vzzT+e0r7/+2kgys2fPdmm7bNky4+npaU6fPp0nNSNzGFFBjlSoUEGvvfaarl69qrfffts5Pb3DMRs2bFDLli0VEhKiwoULq0KFCnr44Yd1/fp1nTx5UiVKlJAkTZw40TmM3q9fP5f17dmzRz179lSxYsVUqVKlDLeVKiYmRrVr15avr6/uuusuzZgxw2V+RocJNm3aJIfD4RzdadmypVatWqVTp065HAZLld5hgYMHD6pbt24qVqyYfH19VbduXc2bNy/d7SxevFhjx45V2bJlFRgYqLZt2+rw4cMZd/wNtm7dqjZt2iggIEB+fn5q2rSpVq1a5Zw/YcIElS9fXpL03HPPyeFwKDw8PMP1Xbp0SR4eHipZsmS68z08/u/Xxq5du/TYY48pPDxchQsXVnh4uHr37q1Tp065LJPazxs2bNDgwYMVEhKiwMBAPfnkk0pISND58+f16KOPqmjRoipTpoxGjRqlP//807l86uGXKVOmaNKkSapQoYJ8fX11zz336Msvv8xUP6X+LzowMFB+fn5q1qxZppeVpKpVq6pp06b64IMPXKZ/8MEH6tGjh4KCgtJd7uOPP1aTJk1UpEgR+fv7q0OHDtq7d69Lm6z248aNG/X3v/9dxYsXV0hIiHr06KGzZ8+6tL3V9+1WVq5cqTNnzqhPnz4u01O/Z99//7169+6toKAglSpVSgMGDFBcXNwt15kXChUqpKJFi8rLy8s57cyZM9q5c6f69OnjMr1p06aqUqWKYmJiXNbRtWtX+fv76913382zunF7BBXkWOfOneXp6aktW7Zk2ObkyZPq0qWLvL299cEHH2j16tWaPHmyihQpoj/++ENlypTR6tWrJUkDBw7Utm3btG3bNr344osu6+nRo4cqV66spUuX6q233rplXfv27dOIESP07LPPKiYmRk2bNtUzzzyjV199Ncufcfbs2WrWrJlKly7trO1Wh5sOHz6spk2b6vvvv9eMGTO0fPly1ahRQ/369dOUKVPStH/++ed16tQpvffee3rnnXf0448/qmvXrkpOTr5lXZs3b1br1q0VFxen999/X4sXL1ZAQIC6du2qjz/+WNJfh8aWL18uSRo+fLi2bduW5hf0jZo0aaKUlBT16NFDa9asUXx8fIZtT548qapVq2r69Olas2aNoqKidO7cOTVs2FC//PJLmvaDBg1SUFCQPvroI73wwgtatGiRBg8erC5duqhOnTpatmyZ+vbtq9dee00zZ85Ms/ysWbO0evVqTZ8+XQsWLJCHh4c6dep020N/CxYsUPv27RUYGKh58+ZpyZIlCg4OVocOHbIUVgYOHKgVK1bo119/lfTXz/mbb77RwIED023/yiuvqHfv3qpRo4aWLFmiDz/8UFevXtV9992nH374IUf9WKhQIS1atEhTpkzRpk2b9MQTT7is71bft1tZtWqVSpYsqRo1aqQ7/+GHH1aVKlX0ySefaPTo0Vq0aJGeffbZ2/ZdSkqKkpKSbvu63T6f3jrPnj2r8ePH68iRI/rXv/7lnH/w4EFJUu3atdMsW7t2bef8VN7e3mmCPmzA6iEd2N+tDv2kKlWqlKlevbrz/fjx412GwZctW2YkmX379mW4jlsd+kld37hx4zKcd6OwsDDjcDjSbK9du3YmMDDQedgoo8MEGzduNJLMxo0bndNudejn5rofe+wx4+Pjk2YIuVOnTsbPz89cuXLFZTudO3d2abdkyRIjyWzbti3d7aVq3LixKVmypLl69apzWlJSkomIiDDly5c3KSkpxpj/O3wxderUW67PGGNSUlLMkCFDjIeHh5FkHA6HqV69unn22WdvezglKSnJXLt2zRQpUsS88cYbzump/Tx8+HCX9g899JCRZKZNm+YyvW7duqZ+/frO96n1ly1b1vz222/O6fHx8SY4ONi0bds2zbZSa01ISDDBwcGma9euLttITk42derUMY0aNbrlZ7qx765evWr8/f3NrFmzjDHG/Pvf/zYVK1Y0KSkpZtiwYS774enTp42Xl1eaz3z16lVTunRp8+ijj2a4zdv149ChQ13aT5kyxUgy586dM8Zk7vuWkerVq5uOHTummZ76PZsyZYrL9KFDhxpfX1/nvpaR1OVv98rK4dUOHTo4lwsMDDTLly93mb9w4cIMv0dPPfWU8fb2TjN97NixxsPDw1y7di3TdSB3MaICtzDG3HJ+3bp15e3traeeekrz5s3L9gmZDz/8cKbb1qxZU3Xq1HGZ9vjjjys+Pl579uzJ1vYza8OGDWrTpo1CQ0Ndpvfr10/Xr19PMwLw4IMPurxP/R/gzUP/N0pISNC3336rnj17yt/f3znd09NTffr00U8//ZTpw0c3cjgceuutt3T8+HHNnj1b/fv3159//qnXX39dNWvW1ObNm51tr127pueee06VK1eWl5eXvLy85O/vr4SEBB06dCjNum++Eqt69eqSpC5duqSZnt5n79Gjh3x9fZ3vU0ePtmzZkuH/xL/55htdvnxZffv2dfmfe0pKijp27KidO3cqISEhU33j7++vRx55RB988IGSkpI0f/589e/fP91Dj2vWrFFSUpKefPJJl+36+vqqRYsWLieNZ7Ufb7e/5OT7dvbs2QwP+2W07d9//z3dq/9u9NRTT2nnzp23ff33v//NdK0zZ87Ujh079Omnn6pDhw7q1auXFi9enKZdRoeG05tesmRJpaSk6Pz585muA7nL6/ZNgFtLSEjQpUuXVKtWrQzbVKpUSevXr9eUKVM0bNgwJSQk6K677tI///lPPfPMM5neVpkyZTLdtnTp0hlOu3TpUqbXkx2XLl1Kt9ayZcumu/2QkBCX9z4+PpKk3377LcNt/PrrrzLGZGk7WREWFqa///3vzvdLlixR79699e9//1s7duyQ9Ffw+/LLL/Xiiy+qYcOGCgwMlMPhUOfOndOtPTg42OW9t7d3htN///33NMtn9DP9448/dO3atXTPE/n5558lST179szws16+fFlFihTJcP6NBg4cqObNm2vSpEm6ePGi8zyqjLbbsGHDdOffeK5PVvvxdvtLTr5vv/32m0sYzOq2M1K6dOlbBqBUWbnE++6773b++8EHH1SnTp00bNgw9erVSx4eHs5a0/seXL58Oc1+J8n52W/3eZB3CCrIsVWrVik5OVktW7a8Zbv77rtP9913n5KTk7Vr1y7NnDlTI0aMUKlSpfTYY49laltZ+SWW3v+IUqel/gJL/aV042WKktI9LyArQkJCdO7cuTTTU094LF68eI7WL0nFihWTh4dHrm8n1aOPPqrIyEjncf24uDh99tlnGj9+vEaPHu1sl5iYqMuXL7ttuzfK6Gfq7e3tMqp0o9Q+mDlzpho3bpxum1KlSmW6hmbNmqlq1ap66aWX1K5duzSjZjdvd9myZQoLC8twfbnVj9n9vhUvXjxXfn4vvfSSJk6ceNt2YWFh2b4HTqNGjbR69WpdvHhRpUqVUkREhCTpwIED6ty5s0vbAwcOOOffKPWzu/O7g5whqCBHTp8+rVGjRikoKEhDhgzJ1DKenp669957Va1aNS1cuFB79uzRY489lun/mWXW999/r/3797sc/lm0aJECAgJUv359SXJe/fLdd9+patWqznYrV65Msz4fH59M19amTRvFxMTo7NmzztENSZo/f778/Pwy/IOZFUWKFNG9996r5cuX69VXX1XhwoUl/XWC4YIFC1S+fHlVqVIly+s9d+5cuqM0165dU2xsrPPzOBwOGWOcP7dU7733XpZOiMyK5cuXa+rUqc6AefXqVf33v//VfffdJ09Pz3SXadasmYoWLaoffvhB//jHP9xSxwsvvKBly5Zp2LBhGbbp0KGDvLy8dOzYsVsessztfszo+5aRatWq6dixYzne7s2eeuqpTN2E8eZ+yCxjjDZv3qyiRYs6/yNSrlw5NWrUSAsWLNCoUaOc+8j27dt1+PBhjRgxIs16jh8/rpCQkCyFV+Quggoy7eDBg87j7BcuXNBXX32l6OhoeXp6KiYmxnl5cXreeustbdiwQV26dFGFChX0+++/Oy/zbNu2raS/zjcICwvTp59+qjZt2ig4OFjFixe/5aW0t1K2bFk9+OCDmjBhgsqUKaMFCxZo3bp1ioqKkp+fn6S/huWrVq2qUaNGKSkpScWKFVNMTIy2bt2aZn21atXS8uXLNWfOHDVo0EAeHh6655570t32+PHj9dlnn6lVq1YaN26cgoODtXDhQq1atUpTpkzJ8FLWrIqMjFS7du3UqlUrjRo1St7e3po9e7YOHjyoxYsXZ+tOqZMmTdLXX3+tXr16qW7duipcuLBOnDihWbNm6dKlS5o6daokKTAwUPfff7+mTp3q/Dlt3rxZ77//vooWLeqWz3czT09PtWvXTiNHjlRKSoqioqIUHx9/y/+p+/v7a+bMmerbt68uX76snj17qmTJkrp48aL279+vixcvas6cOVmq44knnnC5yiY94eHheumllzR27FgdP35cHTt2VLFixfTzzz9rx44dKlKkiCZOnJgr/ZiZ71tGWrZsqZdeeknXr193fk/coWzZsi6hPSe6deumOnXqqG7dugoJCdHZs2c1d+5cbd68WW+++abLpchRUVFq166dHnnkEQ0dOlQXLlzQ6NGjFRERof79+6dZ9/bt29WiRYs75i7DdwRLT+VFvpB6pUHqy9vb25QsWdK0aNHCvPLKK+bChQtplrn5Spxt27aZ7t27m7CwMOPj42NCQkJMixYtzMqVK12WW79+valXr57x8fExkkzfvn1d1nfx4sXbbsuY/7vh27Jly0zNmjWNt7e3CQ8PT3N1iTHGHDlyxLRv394EBgaaEiVKmOHDh5tVq1aluern8uXLpmfPnqZo0aLG4XC4bFPpXK104MAB07VrVxMUFGS8vb1NnTp1THR0tEub1Kt+li5d6jI99UqTm9un56uvvjKtW7c2RYoUMYULFzaNGzc2//3vf9NdX2au+tm+fbsZNmyYqVOnjgkODjaenp6mRIkSpmPHjubzzz93afvTTz+Zhx9+2BQrVswEBASYjh07moMHD5qwsDDnz86YjK8cy+jn2rdvX1OkSJE09UdFRZmJEyea8uXLG29vb1OvXj2zZs0al2UzupJr8+bNpkuXLiY4ONgUKlTIlCtXznTp0iVN398ss31381U/qVasWGFatWplAgMDjY+PjwkLCzM9e/Y069evd7bJaT/efJVaZr9v6Tl69KhxOBxmyZIlLtMz+lm5+wZ7mREVFWUaNmxoihUrZjw9PU1ISIjp0KGD+eyzz9Jtv3btWtO4cWPj6+trgoODzZNPPml+/vnnNO2OHj1qJJlPPvkktz8CssBhzG0u1wAAi508eVIVK1bU1KlTNWrUKKvLueN17dpVSUlJ+uKLL6wuJU+9+OKLmj9/vo4dO+YyKgNrcXkyAMBFZGSk1q9fr507d1pdSp65cuWK3nzzTb3yyiuEFJshqAAAXERERCg6OrpA3UvkxIkTGjNmjB5//HGrS8FNOPQDAABsixEVAABgWwQVAABgW5YGlaSkJL3wwguqWLGiChcurLvuuksvvfSSUlJSrCwLAADYhKWnNkdFRemtt97SvHnzVLNmTe3atUv9+/dXUFBQpp7/kpKSorNnzyogIICb8wAAkE8YY3T16lWVLVvW5blX6bE0qGzbtk3dunVzPjk1PDxcixcv1q5duzK1/NmzZzN8zgYAALC32NhYlS9f/pZtLA0qzZs311tvvaUjR46oSpUq2r9/v7Zu3arp06en2z4xMdHl4XGpFyzFxsYqMDAwL0oGAAA5FB8fr9DQUAUEBNy2raVB5bnnnlNcXJyqVasmT09PJScna9KkSerdu3e67SMjI9N9pkdgYCBBBQCAfCYzp21YejLtxx9/rAULFmjRokXas2eP5s2bp1dffVXz5s1Lt/2YMWMUFxfnfMXGxuZxxQAAIC9ZesO30NBQjR492uVR6f/v//0/LViwQP/73/9uu3x8fLyCgoIUFxfHiAoAAPlEVv5+Wzqicv369TRn+3p6enJ5MgAAkGTxOSpdu3bVpEmTVKFCBdWsWVN79+7VtGnTNGDAACvLAgAANmHpoZ+rV6/qxRdfVExMjC5cuKCyZcuqd+/eGjdunLy9vW+7PId+AADIf7Ly9ztfP5SQoAIAQP6Tb85RAQAAuBWCCgAAsC2CCgAAsC2CCgAAsC2CCgAAsC2CCgAAsC2CCgAAsC2CCgAAsC2CCgAAsC1Ln/UDALml0aT12V52x9i2bqwEQE4wogIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGyL+6gAuC3uSQLAKoyoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA2yKoAAAA27I0qISHh8vhcKR5DRs2zMqyAACATXhZufGdO3cqOTnZ+f7gwYNq166dHnnkEQurAgAAdmFpUClRooTL+8mTJ6tSpUpq0aKFRRUBAAA7sTSo3OiPP/7QggULNHLkSDkcjnTbJCYmKjEx0fk+Pj4+r8oDAAAWsM3JtCtWrNCVK1fUr1+/DNtERkYqKCjI+QoNDc27AgEAQJ6zTVB5//331alTJ5UtWzbDNmPGjFFcXJzzFRsbm4cVAgCAvGaLQz+nTp3S+vXrtXz58lu28/HxkY+PTx5VBQAArGaLoBIdHa2SJUuqS5cuVpcCwM0aTVqf7WV3jG3rxkoA5EeWH/pJSUlRdHS0+vbtKy8vW+QmAABgE5YHlfXr1+v06dMaMGCA1aUAAACbsXwIo3379jLGWF0GAACwIctHVAAAADJCUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZFUAEAALZl+dOTgYKm0aT12V52x9i2bqwEAOyPERUAAGBbBBUAAGBbBBUAAGBbBBUAAGBbBBUAAGBbBBUAAGBbBBUAAGBb3EcFgG3l5J4zAO4MjKgAAADbIqgAAADbIqgAAADbIqgAAADbIqgAAADbIqgAAADbIqgAAADbIqgAAADb4oZvAHCTnNxobsfYtm6sBAAjKgAAwLYIKgAAwLYIKgAAwLYIKgAAwLYsDypnzpzRE088oZCQEPn5+alu3bravXu31WUBAAAbsPSqn19//VXNmjVTq1at9MUXX6hkyZI6duyYihYtamVZAADAJiwNKlFRUQoNDVV0dLRzWnh4uHUFAQAAW7H00M/KlSt1zz336JFHHlHJkiVVr149vfvuuxm2T0xMVHx8vMsLAADcuSwNKsePH9ecOXN09913a82aNXr66af1z3/+U/Pnz0+3fWRkpIKCgpyv0NDQPK4YAADkJUuDSkpKiurXr69XXnlF9erV05AhQzR48GDNmTMn3fZjxoxRXFyc8xUbG5vHFQMAgLxkaVApU6aMatSo4TKtevXqOn36dLrtfXx8FBgY6PICAAB3LkuDSrNmzXT48GGXaUeOHFFYWJhFFQEAADuxNKg8++yz2r59u1555RUdPXpUixYt0jvvvKNhw4ZZWRYAALAJS4NKw4YNFRMTo8WLFysiIkIvv/yypk+frr/97W9WlgUAAGzC0vuoSNIDDzygBx54wOoyAACADVl+C30AAICMEFQAAIBtEVQAAIBtEVQAAIBtEVQAAIBtWX7VD4DMazRpvdUlAECeYkQFAADYFkEFAADYFkEFAADYFkEFAADYFkEFAADYFkEFAADYFkEFAADYFvdRAQA3ysm9bnaMbevGSoA7AyMqAADAtggqAADAtggqAADAtggqAADAtggqAADAtggqAADAtggqAADAtggqAADAtggqAADAtggqAADAtggqAADAtggqAADAtngoIZANOXnwHAAg8xhRAQAAtkVQAQAAtkVQAQAAtkVQAQAAtkVQAQAAtkVQAQAAtkVQAQAAtkVQAQAAtmVpUJkwYYIcDofLq3Tp0laWBAAAbMTyO9PWrFlT69f/310+PT09LawGAADYieVBxcvLi1EUAACQLsvPUfnxxx9VtmxZVaxYUY899piOHz+eYdvExETFx8e7vAAAwJ3L0qBy7733av78+VqzZo3effddnT9/Xk2bNtWlS5fSbR8ZGamgoCDnKzQ0NI8rBgAAeclhjDFWF5EqISFBlSpV0n/+8x+NHDkyzfzExEQlJiY6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nG38/PxUqVIl5/tSpUopPDxc/v7+LtMuXLjgsv0mTZqkeX/o0KF0a929e7eOHj2qgIAA52hQcHCwfv/9d5dDLxkZOHCgli5dqvPnz2vp0qUaMGBAutvYuHGjc/3+/v6qVq2aJDm3cezYMT3++OO66667FBgYqIoVK0qSTp8+7bKu2rVrO/9dpkwZSUrz+QFkn5fVBQDIG76+vmrXrp3atWuncePGadCgQRo/frz69eunU6dOqXPnznr66af18ssvKzg4WFu3btXAgQP1559/OtdRqFAhl3U6HI50p918eCQ9Docj3ekpKSlq0KCBFi5cmGZeiRIlbrveiIgIVatWTb1791b16tUVERGhffv2pdlG165dFRUVlWb51LDRtWtXhYaG6t1331XZsmWVkpKiiIiINIefbvz8qZ8pM58fQOYQVIACqkaNGs57l+zatUtJSUl67bXX5OHx10DrkiVL3Lat7du3p3mfOoJxs/r16+vjjz9WyZIlFRgYmK3tDRgwQEOHDtWcOXMy3MYnn3yi8PBweXml/TV46dIlHTp0SG+//bbuu+8+SXKe9wIgb3HoB7jDXbp0Sa1bt9aCBQv03Xff6cSJE1q6dKmmTJmibt26SZIqVaqkpKQkzZw5U8ePH9eHH36ot956y201fP3115oyZYqOHDmiN998U0uXLtUzzzyTbtu//e1vKl68uLp166avvvpKJ06c0ObNm/XMM8/op59+ytT2Bg8erIsXL2rQoEHpzh82bJguX76s3r17a8eOHTp+/LjWrl2rAQMGKDk52Xm10TvvvKOjR49qw4YNGjlyZLY/P4DsI6gAdzh/f3/de++9ev3113X//fcrIiJCL774ogYPHqxZs2ZJkurWratp06YpKipKERERWrhwoSIjI91Ww7/+9S/t3r1b9erV08svv6zXXntNHTp0SLetn5+ftmzZogoVKqhHjx6qXr26BgwYoN9++y3TIyxeXl4qXrx4uqMl0l/3W/n666+VnJysDh06KCIiQs8884yCgoLk4eEhDw8PffTRR9q9e7ciIiL07LPPaurUqdn+/ACyz2GMMVYXAeDOFR4erhEjRmjEiBFWlwIgH2JEBQAA2BZBBQAA2BaHfgAAgG0xogIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGyLoAIAAGzr/wPOngLr0BX/MQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure()\n",
    "plt.hist(uniform_data, bins=30, density=True, alpha=0.9)  # Fixed 'Tru.' to 'True' and added missing comma\n",
    "plt.xlabel(\"Value\")\n",
    "plt.ylabel(\"Density\")\n",
    "plt.title(\"Uniform Distribution\")\n",
    "plt.show()\n",
    "\n",
    "plt.figure()\n",
    "plt.hist(sample_means, bins=30, density=True, alpha=0.9)\n",
    "plt.xlabel(\"Sample Mean\")\n",
    "plt.ylabel(\"Density\")\n",
    "plt.title(\"Distribution of Sample Means (n = 30)\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a5f7366-2064-4c7a-8a60-02abdb3f3a8c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
