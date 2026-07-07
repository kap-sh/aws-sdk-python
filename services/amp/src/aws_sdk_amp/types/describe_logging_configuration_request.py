"""Generated from Smithy shape ``com.amazonaws.amp#DescribeLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_id


class DescribeLoggingConfigurationRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to describe the logging configuration for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeLoggingConfigurationRequest:
    out: DescribeLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
