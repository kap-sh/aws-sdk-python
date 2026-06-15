"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteHarnessRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.harness_id


class DeleteHarnessRequest(TypedDict):
    harness_id: "aws_sdk_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness to delete.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteHarnessRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteHarnessRequest:
    out: DeleteHarnessRequest = {}  # type: ignore[typeddict-item]
    return out
