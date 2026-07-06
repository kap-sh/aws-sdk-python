"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.resource_detail_arn
    import aws_sdk_service_catalog.types.resource_detail_created_time
    import aws_sdk_service_catalog.types.resource_detail_description
    import aws_sdk_service_catalog.types.resource_detail_id
    import aws_sdk_service_catalog.types.resource_detail_name


class ResourceDetail(TypedDict, closed=True):
    id: NotRequired["aws_sdk_service_catalog.types.resource_detail_id.ResourceDetailId"]
    """<p>The identifier of the resource.</p>"""
    arn: NotRequired[
        "aws_sdk_service_catalog.types.resource_detail_arn.ResourceDetailARN"
    ]
    """<p>The ARN of the resource.</p>"""
    name: NotRequired[
        "aws_sdk_service_catalog.types.resource_detail_name.ResourceDetailName"
    ]
    """<p>The name of the resource.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.resource_detail_description.ResourceDetailDescription"
    ]
    """<p>The description of the resource.</p>"""
    created_time: NotRequired[
        "aws_sdk_service_catalog.types.resource_detail_created_time.ResourceDetailCreatedTime"
    ]
    """<p>The creation time of the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import aws_sdk_service_catalog.types.resource_detail_created_time

        out["CreatedTime"] = (
            aws_sdk_service_catalog.types.resource_detail_created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDetail:
    out: ResourceDetail = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTime" in data:
        import aws_sdk_service_catalog.types.resource_detail_created_time

        out["created_time"] = (
            aws_sdk_service_catalog.types.resource_detail_created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    return out
