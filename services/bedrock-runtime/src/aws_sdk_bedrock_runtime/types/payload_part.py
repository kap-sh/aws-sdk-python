"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#PayloadPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.part_body


class PayloadPart(TypedDict):
    bytes: NotRequired["aws_sdk_bedrock_runtime.types.part_body.PartBody"]
    """<p>Base64-encoded bytes of payload data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> PayloadPart:
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    if "bytes" in data:
        import aws_sdk_bedrock_runtime.types.part_body

        out["bytes"] = aws_sdk_bedrock_runtime.types.part_body.deserialize_json(
            data["bytes"]
        )
    return out
