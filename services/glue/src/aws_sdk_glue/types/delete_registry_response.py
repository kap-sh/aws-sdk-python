"""Generated from Smithy shape ``com.amazonaws.glue#DeleteRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.registry_status
    import aws_sdk_glue.types.schema_registry_name_string


class DeleteRegistryResponse(TypedDict, closed=True):
    registry_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the registry being deleted.</p>"""
    registry_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the registry being deleted.</p>"""
    status: NotRequired["aws_sdk_glue.types.registry_status.RegistryStatus"]
    """<p>The status of the registry. A successful operation will return the <code>Deleting</code> status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegistryResponse) -> dict:
    out: dict = {}
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    if "status" in value:
        import aws_sdk_glue.types.registry_status

        out["Status"] = aws_sdk_glue.types.registry_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegistryResponse:
    out: DeleteRegistryResponse = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    if "Status" in data:
        import aws_sdk_glue.types.registry_status

        out["status"] = aws_sdk_glue.types.registry_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
