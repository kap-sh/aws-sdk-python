"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceCatalog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.resource_catalog_arn
    import capo_sagemaker.types.resource_catalog_description
    import capo_sagemaker.types.resource_catalog_name
    import capo_sagemaker.types.timestamp


class ResourceCatalog(TypedDict, closed=True):
    resource_catalog_arn: NotRequired[
        "capo_sagemaker.types.resource_catalog_arn.ResourceCatalogArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the <code>ResourceCatalog</code>. </p>"""
    resource_catalog_name: NotRequired[
        "capo_sagemaker.types.resource_catalog_name.ResourceCatalogName"
    ]
    """<p> The name of the <code>ResourceCatalog</code>. </p>"""
    description: NotRequired[
        "capo_sagemaker.types.resource_catalog_description.ResourceCatalogDescription"
    ]
    """<p> A free form description of the <code>ResourceCatalog</code>. </p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p> The time the <code>ResourceCatalog</code> was created. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCatalog) -> dict:
    out: dict = {}
    if "resource_catalog_arn" in value:
        out["ResourceCatalogArn"] = value["resource_catalog_arn"]
    if "resource_catalog_name" in value:
        out["ResourceCatalogName"] = value["resource_catalog_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceCatalog:
    out: ResourceCatalog = {}  # type: ignore[typeddict-item]
    if "ResourceCatalogArn" in data:
        out["resource_catalog_arn"] = data["ResourceCatalogArn"]
    if "ResourceCatalogName" in data:
        out["resource_catalog_name"] = data["ResourceCatalogName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
