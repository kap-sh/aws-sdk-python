"""Generated from Smithy shape ``com.amazonaws.synthetics#CreateGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.group


class CreateGroupResponse(TypedDict):
    group: NotRequired["aws_sdk_synthetics.types.group.Group"]
    """<p>A structure that contains information about the group that was just created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_synthetics.types.group

        out["Group"] = aws_sdk_synthetics.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> CreateGroupResponse:
    out: CreateGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_synthetics.types.group

        out["group"] = aws_sdk_synthetics.types.group.deserialize_json(data["Group"])
    return out
