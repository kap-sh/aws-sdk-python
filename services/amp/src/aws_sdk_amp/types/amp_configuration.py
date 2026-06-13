"""Generated from Smithy shape ``com.amazonaws.amp#AmpConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_arn


class AmpConfiguration(TypedDict):
    workspace_arn: "aws_sdk_amp.types.workspace_arn.WorkspaceArn"
    """<p>ARN of the Amazon Managed Service for Prometheus workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmpConfiguration) -> dict:
    out: dict = {}
    out["workspaceArn"] = value["workspace_arn"]
    return out


def deserialize_json(data: dict) -> AmpConfiguration:
    out: AmpConfiguration = {}  # type: ignore[typeddict-item]
    if "workspaceArn" in data:
        out["workspace_arn"] = data["workspaceArn"]
    else:
        raise DeserializationError("AmpConfiguration.workspace_arn required")
    return out
