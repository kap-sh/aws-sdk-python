"""Generated from Smithy shape ``com.amazonaws.amp#DescribeQueryLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.workspace_id


class DescribeQueryLoggingConfigurationRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace for which to retrieve the query logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQueryLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeQueryLoggingConfigurationRequest:
    out: DescribeQueryLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
