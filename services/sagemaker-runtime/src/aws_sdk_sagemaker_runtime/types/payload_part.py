"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#PayloadPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.part_blob


class PayloadPart(TypedDict):
    bytes: NotRequired["aws_sdk_sagemaker_runtime.types.part_blob.PartBlob"]
    """<p>A blob that contains part of the response for your streaming inference request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PayloadPart) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_sagemaker_runtime.types.part_blob

        out["Bytes"] = aws_sdk_sagemaker_runtime.types.part_blob.serialize_json(
            value["bytes"]
        )
    return out


def deserialize_json(data: dict) -> PayloadPart:
    out: PayloadPart = {}  # type: ignore[typeddict-item]
    if "Bytes" in data:
        import aws_sdk_sagemaker_runtime.types.part_blob

        out["bytes"] = aws_sdk_sagemaker_runtime.types.part_blob.deserialize_json(
            data["Bytes"]
        )
    return out
