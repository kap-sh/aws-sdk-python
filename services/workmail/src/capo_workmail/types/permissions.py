"""Generated from Smithy shape ``com.amazonaws.workmail#Permissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.permission

Permissions: TypeAlias = list["capo_workmail.types.permission.Permission"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Permissions) -> list:
    import capo_workmail.types.permission

    out: list = []
    for item in value:
        out.append(capo_workmail.types.permission.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Permissions:
    import capo_workmail.types.permission

    out: Permissions = []
    for item in data:
        out.append(capo_workmail.types.permission.deserialize_aws_json_1_1(item))
    return out
