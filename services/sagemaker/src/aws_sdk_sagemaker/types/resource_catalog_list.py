"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceCatalogList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_catalog

ResourceCatalogList: TypeAlias = list[
    "aws_sdk_sagemaker.types.resource_catalog.ResourceCatalog"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCatalogList) -> list:
    import aws_sdk_sagemaker.types.resource_catalog

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.resource_catalog.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceCatalogList:
    import aws_sdk_sagemaker.types.resource_catalog

    out: ResourceCatalogList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.resource_catalog.deserialize_aws_json_1_1(item)
        )
    return out
