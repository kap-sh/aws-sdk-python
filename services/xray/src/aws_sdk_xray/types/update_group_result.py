"""Generated from Smithy shape ``com.amazonaws.xray#UpdateGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.group


class UpdateGroupResult(TypedDict, closed=True):
    group: NotRequired["aws_sdk_xray.types.group.Group"]
    """<p>The group that was updated. Contains the name of the group that was updated, the ARN of the group that was updated, the updated filter expression, and the updated insight configuration assigned to the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupResult) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_xray.types.group

        out["Group"] = aws_sdk_xray.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> UpdateGroupResult:
    out: UpdateGroupResult = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_xray.types.group

        out["group"] = aws_sdk_xray.types.group.deserialize_json(data["Group"])
    return out
