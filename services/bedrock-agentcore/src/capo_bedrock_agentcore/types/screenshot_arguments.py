"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ScreenshotArguments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.screenshot_format


class ScreenshotArguments(TypedDict, closed=True):
    format: NotRequired[
        "capo_bedrock_agentcore.types.screenshot_format.ScreenshotFormat"
    ]
    """<p>The image format for the screenshot. Defaults to <code>PNG</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScreenshotArguments) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_bedrock_agentcore.types.screenshot_format

        out["format"] = capo_bedrock_agentcore.types.screenshot_format.serialize_json(
            value["format"]
        )
    return out


def deserialize_json(data: dict) -> ScreenshotArguments:
    out: ScreenshotArguments = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import capo_bedrock_agentcore.types.screenshot_format

        out["format"] = capo_bedrock_agentcore.types.screenshot_format.deserialize_json(
            data["format"]
        )
    return out
