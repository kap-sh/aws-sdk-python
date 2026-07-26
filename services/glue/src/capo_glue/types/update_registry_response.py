"""Generated from Smithy shape ``com.amazonaws.glue#UpdateRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_resource_arn
    import capo_glue.types.schema_registry_name_string


class UpdateRegistryResponse(TypedDict, closed=True):
    registry_name: NotRequired[
        "capo_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the updated registry.</p>"""
    registry_arn: NotRequired["capo_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource name (ARN) of the updated registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRegistryResponse) -> dict:
    out: dict = {}
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRegistryResponse:
    out: UpdateRegistryResponse = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    return out
