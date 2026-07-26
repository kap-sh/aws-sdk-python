"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceCatalogList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.resource_catalog

ResourceCatalogList: TypeAlias = list[
    "capo_sagemaker.types.resource_catalog.ResourceCatalog"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCatalogList) -> list:
    import capo_sagemaker.types.resource_catalog

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.resource_catalog.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceCatalogList:
    import capo_sagemaker.types.resource_catalog

    out: ResourceCatalogList = []
    for item in data:
        out.append(capo_sagemaker.types.resource_catalog.deserialize_aws_json_1_1(item))
    return out
