"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Attribution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.citations


class Attribution(TypedDict):
    citations: NotRequired["aws_sdk_bedrock_agent_runtime.types.citations.Citations"]
    """<p>A list of citations and related information for a part of an agent response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attribution) -> dict:
    out: dict = {}
    if "citations" in value:
        import aws_sdk_bedrock_agent_runtime.types.citations

        out["citations"] = aws_sdk_bedrock_agent_runtime.types.citations.serialize_json(
            value["citations"]
        )
    return out


def deserialize_json(data: dict) -> Attribution:
    out: Attribution = {}  # type: ignore[typeddict-item]
    if "citations" in data:
        import aws_sdk_bedrock_agent_runtime.types.citations

        out["citations"] = (
            aws_sdk_bedrock_agent_runtime.types.citations.deserialize_json(
                data["citations"]
            )
        )
    return out
