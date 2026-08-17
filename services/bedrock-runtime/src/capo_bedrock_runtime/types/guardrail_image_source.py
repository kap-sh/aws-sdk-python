"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailImageSource``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError


class _GuardrailImageSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


GuardrailImageSource: TypeAlias = _GuardrailImageSource_bytes


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailImageSource) -> dict:
    if "bytes" in value:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    else:
        raise SerializationError("GuardrailImageSource: no variant present")


def deserialize_json(data: dict) -> GuardrailImageSource:
    if data.get("bytes") is not None:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    else:
        raise DeserializationError("GuardrailImageSource: no recognized variant key")
