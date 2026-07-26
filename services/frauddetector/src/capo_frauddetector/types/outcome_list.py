"""Generated from Smithy shape ``com.amazonaws.frauddetector#OutcomeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.outcome

OutcomeList: TypeAlias = list["capo_frauddetector.types.outcome.Outcome"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutcomeList) -> list:
    import capo_frauddetector.types.outcome

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.outcome.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OutcomeList:
    import capo_frauddetector.types.outcome

    out: OutcomeList = []
    for item in data:
        out.append(capo_frauddetector.types.outcome.deserialize_aws_json_1_1(item))
    return out
