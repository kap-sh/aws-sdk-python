"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedOperatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.operators

SupportedOperatorList: TypeAlias = list["aws_sdk_appflow.types.operators.Operators"]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedOperatorList) -> list:
    import aws_sdk_appflow.types.operators

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.operators.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportedOperatorList:
    import aws_sdk_appflow.types.operators

    out: SupportedOperatorList = []
    for item in data:
        out.append(aws_sdk_appflow.types.operators.deserialize_json(item))
    return out
