from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


class Constants(BaseConstants):
    name_in_url = "trust"
    players_per_group = 2
    num_rounds = 1
    endowment = c(10)
    multiplier = 3
    instructions_template = "trust/instructions.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        doc="Amount sent by P1", max=Constants.endowment, min=0
    )
    sent_back_amount = models.CurrencyField(doc="Amount sent back by P2")

    def sent_back_amount_choices(self):
        return currency_range(c(0), self.sent_amount * Constants.multiplier, c(1))


class Player(BasePlayer):
    pass
