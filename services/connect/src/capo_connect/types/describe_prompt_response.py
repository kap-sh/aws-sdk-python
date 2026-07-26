"""Generated from Smithy shape ``com.amazonaws.connect#DescribePromptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.prompt


class DescribePromptResponse(TypedDict, closed=True):
    prompt: NotRequired["capo_connect.types.prompt.Prompt"]
    """<p>Information about the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePromptResponse) -> dict:
    out: dict = {}
    if "prompt" in value:
        import capo_connect.types.prompt

        out["Prompt"] = capo_connect.types.prompt.serialize_json(value["prompt"])
    return out


def deserialize_json(data: dict) -> DescribePromptResponse:
    out: DescribePromptResponse = {}  # type: ignore[typeddict-item]
    if "Prompt" in data:
        import capo_connect.types.prompt

        out["prompt"] = capo_connect.types.prompt.deserialize_json(data["Prompt"])
    return out
