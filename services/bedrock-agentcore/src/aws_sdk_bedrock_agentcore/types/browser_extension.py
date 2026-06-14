"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserExtension``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.resource_location


class BrowserExtension(TypedDict):
    location: "aws_sdk_bedrock_agentcore.types.resource_location.ResourceLocation"
    """<p>The location where the browser extension files are stored. This specifies the source from which the extension will be loaded and installed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserExtension) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.resource_location

    out["location"] = aws_sdk_bedrock_agentcore.types.resource_location.serialize_json(
        value["location"]
    )
    return out


def deserialize_json(data: dict) -> BrowserExtension:
    out: BrowserExtension = {}  # type: ignore[typeddict-item]
    if "location" in data:
        import aws_sdk_bedrock_agentcore.types.resource_location

        out["location"] = (
            aws_sdk_bedrock_agentcore.types.resource_location.deserialize_json(
                data["location"]
            )
        )
    else:
        raise DeserializationError("BrowserExtension.location required")
    return out
