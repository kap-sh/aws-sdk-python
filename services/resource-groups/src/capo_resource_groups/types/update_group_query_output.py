"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UpdateGroupQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_query


class UpdateGroupQueryOutput(TypedDict, closed=True):
    group_query: NotRequired["capo_resource_groups.types.group_query.GroupQuery"]
    """<p>The updated resource query associated with the resource group after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupQueryOutput) -> dict:
    out: dict = {}
    if "group_query" in value:
        import capo_resource_groups.types.group_query

        out["GroupQuery"] = capo_resource_groups.types.group_query.serialize_json(
            value["group_query"]
        )
    return out


def deserialize_json(data: dict) -> UpdateGroupQueryOutput:
    out: UpdateGroupQueryOutput = {}  # type: ignore[typeddict-item]
    if "GroupQuery" in data:
        import capo_resource_groups.types.group_query

        out["group_query"] = capo_resource_groups.types.group_query.deserialize_json(
            data["GroupQuery"]
        )
    return out
