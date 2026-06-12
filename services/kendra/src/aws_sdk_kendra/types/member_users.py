"""Generated from Smithy shape ``com.amazonaws.kendra#MemberUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.member_user

MemberUsers: TypeAlias = list["aws_sdk_kendra.types.member_user.MemberUser"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberUsers) -> list:
    import aws_sdk_kendra.types.member_user

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.member_user.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MemberUsers:
    import aws_sdk_kendra.types.member_user

    out: MemberUsers = []
    for item in data:
        out.append(aws_sdk_kendra.types.member_user.deserialize_aws_json_1_1(item))
    return out
