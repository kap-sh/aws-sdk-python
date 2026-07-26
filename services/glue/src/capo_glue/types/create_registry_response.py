"""Generated from Smithy shape ``com.amazonaws.glue#CreateRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.glue_resource_arn
    import capo_glue.types.schema_registry_name_string
    import capo_glue.types.tags_map


class CreateRegistryResponse(TypedDict, closed=True):
    registry_arn: NotRequired["capo_glue.types.glue_resource_arn.GlueResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the newly created registry.</p>"""
    registry_name: NotRequired[
        "capo_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    ]
    """<p>The name of the registry.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the registry.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The tags for the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRegistryResponse) -> dict:
    out: dict = {}
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRegistryResponse:
    out: CreateRegistryResponse = {}  # type: ignore[typeddict-item]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
