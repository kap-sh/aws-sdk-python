"""Generated from Smithy shape ``com.amazonaws.schemas#RegistrySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__string
    import capo_schemas.types.tags


class RegistrySummary(TypedDict, closed=True):
    registry_arn: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ARN of the registry.</p>"""
    registry_name: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The name of the registry.</p>"""
    tags: NotRequired["capo_schemas.types.tags.Tags"]
    """<p>Tags associated with the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistrySummary) -> dict:
    out: dict = {}
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    if "tags" in value:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegistrySummary:
    out: RegistrySummary = {}  # type: ignore[typeddict-item]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    if "tags" in data:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.deserialize_json(data["tags"])
    return out
