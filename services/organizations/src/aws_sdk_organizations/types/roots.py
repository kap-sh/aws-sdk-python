"""Generated from Smithy shape ``com.amazonaws.organizations#Roots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.root

Roots: TypeAlias = list["aws_sdk_organizations.types.root.Root"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Roots) -> list:
    import aws_sdk_organizations.types.root

    out: list = []
    for item in value:
        out.append(aws_sdk_organizations.types.root.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Roots:
    import aws_sdk_organizations.types.root

    out: Roots = []
    for item in data:
        out.append(aws_sdk_organizations.types.root.deserialize_aws_json_1_1(item))
    return out
