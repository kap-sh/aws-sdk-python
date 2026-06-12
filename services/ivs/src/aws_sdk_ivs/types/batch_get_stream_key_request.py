"""Generated from Smithy shape ``com.amazonaws.ivs#BatchGetStreamKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_key_arn_list


class BatchGetStreamKeyRequest(TypedDict):
    arns: "aws_sdk_ivs.types.stream_key_arn_list.StreamKeyArnList"
    """<p>Array of ARNs, one per stream key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStreamKeyRequest) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.stream_key_arn_list

    out["arns"] = aws_sdk_ivs.types.stream_key_arn_list.serialize_json(value["arns"])
    return out


def deserialize_json(data: dict) -> BatchGetStreamKeyRequest:
    out: BatchGetStreamKeyRequest = {}  # type: ignore[typeddict-item]
    if "arns" in data:
        import aws_sdk_ivs.types.stream_key_arn_list

        out["arns"] = aws_sdk_ivs.types.stream_key_arn_list.deserialize_json(
            data["arns"]
        )
    else:
        raise DeserializationError("BatchGetStreamKeyRequest.arns required")
    return out
