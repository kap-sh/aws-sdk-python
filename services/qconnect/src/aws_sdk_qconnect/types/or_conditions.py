"""Generated from Smithy shape ``com.amazonaws.qconnect#OrConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.or_condition

OrConditions: TypeAlias = list["aws_sdk_qconnect.types.or_condition.OrCondition"]


# --- restJson1 ser/de ---
def serialize_json(value: OrConditions) -> list:
    import aws_sdk_qconnect.types.or_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.or_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrConditions:
    import aws_sdk_qconnect.types.or_condition

    out: OrConditions = []
    for item in data:
        out.append(aws_sdk_qconnect.types.or_condition.deserialize_json(item))
    return out
