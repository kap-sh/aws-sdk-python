"""Generated from Smithy shape ``com.amazonaws.synthetics#GetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.group_identifier


class GetGroupRequest(TypedDict, closed=True):
    group_identifier: "capo_synthetics.types.group_identifier.GroupIdentifier"
    """<p>Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGroupRequest:
    out: GetGroupRequest = {}  # type: ignore[typeddict-item]
    return out
