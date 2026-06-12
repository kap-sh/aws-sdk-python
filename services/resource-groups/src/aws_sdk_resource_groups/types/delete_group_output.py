"""Generated from Smithy shape ``com.amazonaws.resourcegroups#DeleteGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group


class DeleteGroupOutput(TypedDict):
    group: NotRequired["aws_sdk_resource_groups.types.group.Group"]
    """<p>A full description of the deleted resource group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGroupOutput) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_resource_groups.types.group

        out["Group"] = aws_sdk_resource_groups.types.group.serialize_json(
            value["group"]
        )
    return out


def deserialize_json(data: dict) -> DeleteGroupOutput:
    out: DeleteGroupOutput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_resource_groups.types.group

        out["group"] = aws_sdk_resource_groups.types.group.deserialize_json(
            data["Group"]
        )
    return out
