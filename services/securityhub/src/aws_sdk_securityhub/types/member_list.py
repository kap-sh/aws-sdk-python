"""Generated from Smithy shape ``com.amazonaws.securityhub#MemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.member

MemberList: TypeAlias = list["aws_sdk_securityhub.types.member.Member"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberList) -> list:
    import aws_sdk_securityhub.types.member

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.member.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberList:
    import aws_sdk_securityhub.types.member

    out: MemberList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.member.deserialize_json(item))
    return out
