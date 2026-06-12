"""Generated from Smithy shape ``com.amazonaws.identitystore#Roles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.role

Roles: TypeAlias = list["aws_sdk_identitystore.types.role.Role"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Roles) -> list:
    import aws_sdk_identitystore.types.role

    out: list = []
    for item in value:
        out.append(aws_sdk_identitystore.types.role.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Roles:
    import aws_sdk_identitystore.types.role

    out: Roles = []
    for item in data:
        out.append(aws_sdk_identitystore.types.role.deserialize_aws_json_1_1(item))
    return out
