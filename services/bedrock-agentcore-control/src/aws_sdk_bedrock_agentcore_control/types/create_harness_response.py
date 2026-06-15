"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateHarnessResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness


class CreateHarnessResponse(TypedDict):
    harness: "aws_sdk_bedrock_agentcore_control.types.harness.Harness"
    """<p>The harness that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHarnessResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.harness

    out["harness"] = aws_sdk_bedrock_agentcore_control.types.harness.serialize_json(
        value["harness"]
    )
    return out


def deserialize_json(data: dict) -> CreateHarnessResponse:
    out: CreateHarnessResponse = {}  # type: ignore[typeddict-item]
    if "harness" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness

        out["harness"] = (
            aws_sdk_bedrock_agentcore_control.types.harness.deserialize_json(
                data["harness"]
            )
        )
    else:
        raise DeserializationError("CreateHarnessResponse.harness required")
    return out
