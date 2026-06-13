"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#BidirectionalInputPayloadPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.part_body


class BidirectionalInputPayloadPart(TypedDict):
    bytes: NotRequired["aws_sdk_bedrock_runtime.types.part_body.PartBody"]
    """<p>The audio content for the bidirectional input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BidirectionalInputPayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> BidirectionalInputPayloadPart:
    out: BidirectionalInputPayloadPart = {}  # type: ignore[typeddict-item]
    if "bytes" in data:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.deserialize_json(
            data["bytes"]
        )
    return out
