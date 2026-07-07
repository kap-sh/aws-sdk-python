"""Generated from Smithy shape ``com.amazonaws.glue#CreateRegistryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.schema_registry_name_string
    import aws_sdk_glue.types.tags_map


class CreateRegistryInput(TypedDict, closed=True):
    registry_name: (
        "aws_sdk_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    )
    """<p>Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the registry. If description is not provided, there will not be any default value for this.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRegistryInput) -> dict:
    out: dict = {}
    out["RegistryName"] = value["registry_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRegistryInput:
    out: CreateRegistryInput = {}  # type: ignore[typeddict-item]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    else:
        raise DeserializationError("CreateRegistryInput.registry_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
