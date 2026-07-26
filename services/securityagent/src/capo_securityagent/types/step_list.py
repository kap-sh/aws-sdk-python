"""Generated from Smithy shape ``com.amazonaws.securityagent#StepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.step

StepList: TypeAlias = list["capo_securityagent.types.step.Step"]


# --- restJson1 ser/de ---
def serialize_json(value: StepList) -> list:
    import capo_securityagent.types.step

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.step.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepList:
    import capo_securityagent.types.step

    out: StepList = []
    for item in data:
        out.append(capo_securityagent.types.step.deserialize_json(item))
    return out
