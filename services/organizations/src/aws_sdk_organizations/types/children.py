"""Generated from Smithy shape ``com.amazonaws.organizations#Children``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.child

Children: TypeAlias = list["aws_sdk_organizations.types.child.Child"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Children) -> list:
    import aws_sdk_organizations.types.child

    out: list = []
    for item in value:
        out.append(aws_sdk_organizations.types.child.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Children:
    import aws_sdk_organizations.types.child

    out: Children = []
    for item in data:
        out.append(aws_sdk_organizations.types.child.deserialize_aws_json_1_1(item))
    return out
