"""Generated from Smithy shape ``com.amazonaws.connect#DescribePromptResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.prompt


class DescribePromptResponse(TypedDict):
    prompt: NotRequired["aws_sdk_connect.types.prompt.Prompt"]
    """<p>Information about the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePromptResponse) -> dict:
    out: dict = {}
    if "prompt" in value:
        import aws_sdk_connect.types.prompt

        out["Prompt"] = aws_sdk_connect.types.prompt.serialize_json(value["prompt"])
    return out


def deserialize_json(data: dict) -> DescribePromptResponse:
    out: DescribePromptResponse = {}  # type: ignore[typeddict-item]
    if "Prompt" in data:
        import aws_sdk_connect.types.prompt

        out["prompt"] = aws_sdk_connect.types.prompt.deserialize_json(data["Prompt"])
    return out
