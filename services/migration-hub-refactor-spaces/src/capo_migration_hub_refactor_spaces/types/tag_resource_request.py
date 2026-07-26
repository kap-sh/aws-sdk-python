"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.string
    import capo_migration_hub_refactor_spaces.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_migration_hub_refactor_spaces.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_migration_hub_refactor_spaces.types.tag_map.TagMap"
    """<p>The new or modified tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_migration_hub_refactor_spaces.types.tag_map

    out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
