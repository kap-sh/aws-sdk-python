"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetHarnessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness


class GetHarnessResponse(TypedDict, closed=True):
    harness: "aws_sdk_bedrock_agentcore_control.types.harness.Harness"
    """<p>The harness resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHarnessResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.harness

    out["harness"] = aws_sdk_bedrock_agentcore_control.types.harness.serialize_json(
        value["harness"]
    )
    return out


def deserialize_json(data: dict) -> GetHarnessResponse:
    out: GetHarnessResponse = {}  # type: ignore[typeddict-item]
    if "harness" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness

        out["harness"] = (
            aws_sdk_bedrock_agentcore_control.types.harness.deserialize_json(
                data["harness"]
            )
        )
    else:
        raise DeserializationError("GetHarnessResponse.harness required")
    return out
