"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.resource_detail

ResourceDetails: TypeAlias = list[
    "capo_service_catalog.types.resource_detail.ResourceDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDetails) -> list:
    import capo_service_catalog.types.resource_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.resource_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceDetails:
    import capo_service_catalog.types.resource_detail

    out: ResourceDetails = []
    for item in data:
        out.append(
            capo_service_catalog.types.resource_detail.deserialize_aws_json_1_1(item)
        )
    return out
