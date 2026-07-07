"""Generated from Smithy shape ``com.amazonaws.glue#RegistryId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.schema_registry_name_string


class RegistryId(TypedDict, closed=True):
    registry_name: NotRequired[
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>Name of the registry. Used only for lookup. One of <code>RegistryArn</code> or <code>RegistryName</code> has to be provided. </p>"""
    registry_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>Arn of the registry to be updated. One of <code>RegistryArn</code> or <code>RegistryName</code> has to be provided.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryId) -> dict:
    out: dict = {}
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryId:
    out: RegistryId = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    return out
