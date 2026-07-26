"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfFailoverCondition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.failover_condition

__listOfFailoverCondition: TypeAlias = list[
    "capo_medialive.types.failover_condition.FailoverCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFailoverCondition) -> list:
    import capo_medialive.types.failover_condition

    out: list = []
    for item in value:
        out.append(capo_medialive.types.failover_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFailoverCondition:
    import capo_medialive.types.failover_condition

    out: __listOfFailoverCondition = []
    for item in data:
        out.append(capo_medialive.types.failover_condition.deserialize_json(item))
    return out
