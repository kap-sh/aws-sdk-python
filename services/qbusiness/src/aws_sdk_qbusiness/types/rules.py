"""Generated from Smithy shape ``com.amazonaws.qbusiness#Rules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.rule

Rules: TypeAlias = list["aws_sdk_qbusiness.types.rule.Rule"]


# --- restJson1 ser/de ---
def serialize_json(value: Rules) -> list:
    import aws_sdk_qbusiness.types.rule

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> Rules:
    import aws_sdk_qbusiness.types.rule

    out: Rules = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.rule.deserialize_json(item))
    return out
