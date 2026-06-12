"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceChangeDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.resource_change_detail

ResourceChangeDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.resource_change_detail.ResourceChangeDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceChangeDetails) -> list:
    import aws_sdk_service_catalog.types.resource_change_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.resource_change_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceChangeDetails:
    import aws_sdk_service_catalog.types.resource_change_detail

    out: ResourceChangeDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.resource_change_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
