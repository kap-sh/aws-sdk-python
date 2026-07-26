"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockStart``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.image_block_start
    import capo_bedrock_runtime.types.tool_result_block_start
    import capo_bedrock_runtime.types.tool_use_block_start


class _ContentBlockStart_toolUse(TypedDict, closed=True):
    toolUse: "capo_bedrock_runtime.types.tool_use_block_start.ToolUseBlockStart"


class _ContentBlockStart_toolResult(TypedDict, closed=True):
    toolResult: (
        "capo_bedrock_runtime.types.tool_result_block_start.ToolResultBlockStart"
    )


class _ContentBlockStart_image(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.image_block_start.ImageBlockStart"


ContentBlockStart: TypeAlias = (
    _ContentBlockStart_toolUse
    | _ContentBlockStart_toolResult
    | _ContentBlockStart_image
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockStart) -> dict:
    if "toolUse" in value:
        import capo_bedrock_runtime.types.tool_use_block_start

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_start.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_runtime.types.tool_result_block_start

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_block_start.serialize_json(
                value["toolResult"]
            )
        }
    elif "image" in value:
        import capo_bedrock_runtime.types.image_block_start

        return {
            "image": capo_bedrock_runtime.types.image_block_start.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("ContentBlockStart: no variant present")


def deserialize_json(data: dict) -> ContentBlockStart:
    if "toolUse" in data:
        import capo_bedrock_runtime.types.tool_use_block_start

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_start.deserialize_json(
                data["toolUse"]
            )
        }
    elif "toolResult" in data:
        import capo_bedrock_runtime.types.tool_result_block_start

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_block_start.deserialize_json(
                data["toolResult"]
            )
        }
    elif "image" in data:
        import capo_bedrock_runtime.types.image_block_start

        return {
            "image": capo_bedrock_runtime.types.image_block_start.deserialize_json(
                data["image"]
            )
        }
    else:
        raise DeserializationError("ContentBlockStart: no recognized variant key")
