"""Generated from Smithy shape ``com.amazonaws.synthetics#DeleteGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.group_identifier


class DeleteGroupRequest(TypedDict):
    group_identifier: "aws_sdk_synthetics.types.group_identifier.GroupIdentifier"
    """<p>Specifies which group to delete. You can specify the group name, the ARN, or the group ID as the <code>GroupIdentifier</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGroupRequest:
    out: DeleteGroupRequest = {}  # type: ignore[typeddict-item]
    return out
