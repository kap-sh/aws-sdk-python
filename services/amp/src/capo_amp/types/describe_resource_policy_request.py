"""Generated from Smithy shape ``com.amazonaws.amp#DescribeResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.workspace_id


class DescribeResourcePolicyRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to describe the resource-based policy for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeResourcePolicyRequest:
    out: DescribeResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
