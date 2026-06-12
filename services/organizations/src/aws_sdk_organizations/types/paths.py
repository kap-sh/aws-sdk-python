"""Generated from Smithy shape ``com.amazonaws.organizations#Paths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.path

Paths: TypeAlias = list["aws_sdk_organizations.types.path.Path"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Paths) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Paths:
    return list(data)
