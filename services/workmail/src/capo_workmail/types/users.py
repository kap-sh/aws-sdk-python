"""Generated from Smithy shape ``com.amazonaws.workmail#Users``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.user

Users: TypeAlias = list["capo_workmail.types.user.User"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Users) -> list:
    import capo_workmail.types.user

    out: list = []
    for item in value:
        out.append(capo_workmail.types.user.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Users:
    import capo_workmail.types.user

    out: Users = []
    for item in data:
        out.append(capo_workmail.types.user.deserialize_aws_json_1_1(item))
    return out
