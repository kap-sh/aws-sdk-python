"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateHarnessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness


class UpdateHarnessResponse(TypedDict, closed=True):
    harness: "aws_sdk_bedrock_agentcore_control.types.harness.Harness"
    """<p>The updated harness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHarnessResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.harness

    out["harness"] = aws_sdk_bedrock_agentcore_control.types.harness.serialize_json(
        value["harness"]
    )
    return out


def deserialize_json(data: dict) -> UpdateHarnessResponse:
    out: UpdateHarnessResponse = {}  # type: ignore[typeddict-item]
    if "harness" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness

        out["harness"] = (
            aws_sdk_bedrock_agentcore_control.types.harness.deserialize_json(
                data["harness"]
            )
        )
    else:
        raise DeserializationError("UpdateHarnessResponse.harness required")
    return out
