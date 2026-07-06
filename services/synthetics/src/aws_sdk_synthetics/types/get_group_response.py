"""Generated from Smithy shape ``com.amazonaws.synthetics#GetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.group


class GetGroupResponse(TypedDict, closed=True):
    group: NotRequired["aws_sdk_synthetics.types.group.Group"]
    """<p>A structure that contains information about the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_synthetics.types.group

        out["Group"] = aws_sdk_synthetics.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> GetGroupResponse:
    out: GetGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_synthetics.types.group

        out["group"] = aws_sdk_synthetics.types.group.deserialize_json(data["Group"])
    return out
