"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group


class GetGroupOutput(TypedDict):
    group: NotRequired["aws_sdk_resource_groups.types.group.Group"]
    """<p>A structure that contains the metadata details for the specified resource group. Use <a>GetGroupQuery</a> and <a>GetGroupConfiguration</a> to get those additional details of the resource group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupOutput) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_resource_groups.types.group

        out["Group"] = aws_sdk_resource_groups.types.group.serialize_json(
            value["group"]
        )
    return out


def deserialize_json(data: dict) -> GetGroupOutput:
    out: GetGroupOutput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_resource_groups.types.group

        out["group"] = aws_sdk_resource_groups.types.group.deserialize_json(
            data["Group"]
        )
    return out
