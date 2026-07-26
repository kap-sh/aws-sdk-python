"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.construct_properties
    import capo_mgn.types.segment_construct_name


class UpdateOperation(TypedDict, closed=True):
    name: NotRequired["capo_mgn.types.segment_construct_name.SegmentConstructName"]
    """<p>The updated name for the construct.</p>"""
    excluded: NotRequired["bool"]
    """<p>Whether to exclude this construct from the migration.</p>"""
    properties: NotRequired["capo_mgn.types.construct_properties.ConstructProperties"]
    """<p>The properties to update on the construct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOperation) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    if "properties" in value:
        import capo_mgn.types.construct_properties

        out["properties"] = capo_mgn.types.construct_properties.serialize_json(
            value["properties"]
        )
    return out


def deserialize_json(data: dict) -> UpdateOperation:
    out: UpdateOperation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "excluded" in data:
        out["excluded"] = data["excluded"]
    if "properties" in data:
        import capo_mgn.types.construct_properties

        out["properties"] = capo_mgn.types.construct_properties.deserialize_json(
            data["properties"]
        )
    return out
