"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.member_specification

MemberList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.member_specification.MemberSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberList) -> list:
    import aws_sdk_cleanrooms.types.member_specification

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.member_specification.serialize_json(item))
    return out


def deserialize_json(data: list) -> MemberList:
    import aws_sdk_cleanrooms.types.member_specification

    out: MemberList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.member_specification.deserialize_json(item))
    return out
