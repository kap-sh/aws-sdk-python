"""Generated from Smithy shape ``com.amazonaws.guardduty#Members``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.member

Members: TypeAlias = list["aws_sdk_guardduty.types.member.Member"]


# --- restJson1 ser/de ---
def serialize_json(value: Members) -> list:
    import aws_sdk_guardduty.types.member

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.member.serialize_json(item))
    return out


def deserialize_json(data: list) -> Members:
    import aws_sdk_guardduty.types.member

    out: Members = []
    for item in data:
        out.append(aws_sdk_guardduty.types.member.deserialize_json(item))
    return out
