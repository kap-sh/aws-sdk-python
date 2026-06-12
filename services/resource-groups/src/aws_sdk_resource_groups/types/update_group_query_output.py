"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UpdateGroupQueryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_query


class UpdateGroupQueryOutput(TypedDict):
    group_query: NotRequired["aws_sdk_resource_groups.types.group_query.GroupQuery"]
    """<p>The updated resource query associated with the resource group after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupQueryOutput) -> dict:
    out: dict = {}
    if "group_query" in value:
        import aws_sdk_resource_groups.types.group_query

        out["GroupQuery"] = aws_sdk_resource_groups.types.group_query.serialize_json(
            value["group_query"]
        )
    return out


def deserialize_json(data: dict) -> UpdateGroupQueryOutput:
    out: UpdateGroupQueryOutput = {}  # type: ignore[typeddict-item]
    if "GroupQuery" in data:
        import aws_sdk_resource_groups.types.group_query

        out["group_query"] = aws_sdk_resource_groups.types.group_query.deserialize_json(
            data["GroupQuery"]
        )
    return out
