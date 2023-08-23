from statemachine import StateMachine, State
from statemachine.exceptions import TransitionNotAllowed


class VendingMachine(StateMachine):
    "A vending machine"
    idle = State(initial=True, value="Idle")
    waiting = State(value="Waiting")
    vended = State(value="Vended")
    refunded = State(value="Refunded")

    insert_coin = idle.to(waiting) | refunded.to(waiting) | vended.to(waiting)
    vend = waiting.to(vended)
    refund = waiting.to(refunded)
    reset = refunded.to(idle) | vended.to(idle)
