"""Generated from Smithy shape ``com.amazonaws.glue#GetRegistryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.created_timestamp
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.registry_status
    import aws_sdk_glue.types.schema_registry_name_string
    import aws_sdk_glue.types.updated_timestamp


class GetRegistryResponse(TypedDict):
    registry_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the registry.</p>"""
    registry_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the registry.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the registry.</p>"""
    status: NotRequired["aws_sdk_glue.types.registry_status.RegistryStatus"]
    """<p>The status of the registry.</p>"""
    created_time: NotRequired["aws_sdk_glue.types.created_timestamp.CreatedTimestamp"]
    """<p>The date and time the registry was created.</p>"""
    updated_time: NotRequired["aws_sdk_glue.types.updated_timestamp.UpdatedTimestamp"]
    """<p>The date and time the registry was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegistryResponse) -> dict:
    out: dict = {}
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_glue.types.registry_status

        out["Status"] = aws_sdk_glue.types.registry_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "updated_time" in value:
        out["UpdatedTime"] = value["updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegistryResponse:
    out: GetRegistryResponse = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_glue.types.registry_status

        out["status"] = aws_sdk_glue.types.registry_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreatedTime" in data:
        out["created_time"] = data["CreatedTime"]
    if "UpdatedTime" in data:
        out["updated_time"] = data["UpdatedTime"]
    return out
