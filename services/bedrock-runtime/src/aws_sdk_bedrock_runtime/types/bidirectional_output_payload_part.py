"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#BidirectionalOutputPayloadPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.part_body


class BidirectionalOutputPayloadPart(TypedDict):
    bytes: NotRequired["aws_sdk_bedrock_runtime.types.part_body.PartBody"]
    """<p>The speech output of the bidirectional stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BidirectionalOutputPayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> BidirectionalOutputPayloadPart:
    out: BidirectionalOutputPayloadPart = {}  # type: ignore[typeddict-item]
    if "bytes" in data:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.deserialize_json(
            data["bytes"]
        )
    return out
