"""Generated from Smithy shape ``com.amazonaws.schemas#CreateRegistryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.tags


class CreateRegistryResponse(TypedDict, closed=True):
    description: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The description of the registry.</p>"""
    registry_arn: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The ARN of the registry.</p>"""
    registry_name: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The name of the registry.</p>"""
    tags: NotRequired["aws_sdk_schemas.types.tags.Tags"]
    """<p>Tags associated with the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "tags" in value:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRegistryResponse:
    out: CreateRegistryResponse = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "tags" in data:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.deserialize_json(data["tags"])
    return out
