"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteHarnessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness


class DeleteHarnessResponse(TypedDict, closed=True):
    harness: NotRequired["aws_sdk_bedrock_agentcore_control.types.harness.Harness"]
    """<p>The harness that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteHarnessResponse) -> dict:
    out: dict = {}
    if "harness" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness

        out["harness"] = aws_sdk_bedrock_agentcore_control.types.harness.serialize_json(
            value["harness"]
        )
    return out


def deserialize_json(data: dict) -> DeleteHarnessResponse:
    out: DeleteHarnessResponse = {}  # type: ignore[typeddict-item]
    if "harness" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness

        out["harness"] = (
            aws_sdk_bedrock_agentcore_control.types.harness.deserialize_json(
                data["harness"]
            )
        )
    return out
