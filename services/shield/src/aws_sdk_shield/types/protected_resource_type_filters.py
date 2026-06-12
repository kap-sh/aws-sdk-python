"""Generated from Smithy shape ``com.amazonaws.shield#ProtectedResourceTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.protected_resource_type

ProtectedResourceTypeFilters: TypeAlias = list[
    "aws_sdk_shield.types.protected_resource_type.ProtectedResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectedResourceTypeFilters) -> list:
    import aws_sdk_shield.types.protected_resource_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_shield.types.protected_resource_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectedResourceTypeFilters:
    import aws_sdk_shield.types.protected_resource_type

    out: ProtectedResourceTypeFilters = []
    for item in data:
        out.append(
            aws_sdk_shield.types.protected_resource_type.deserialize_aws_json_1_1(item)
        )
    return out
