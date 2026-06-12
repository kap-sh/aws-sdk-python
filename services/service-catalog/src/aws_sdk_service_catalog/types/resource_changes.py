"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.resource_change

ResourceChanges: TypeAlias = list[
    "aws_sdk_service_catalog.types.resource_change.ResourceChange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceChanges) -> list:
    import aws_sdk_service_catalog.types.resource_change

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.resource_change.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceChanges:
    import aws_sdk_service_catalog.types.resource_change

    out: ResourceChanges = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.resource_change.deserialize_aws_json_1_1(item)
        )
    return out
