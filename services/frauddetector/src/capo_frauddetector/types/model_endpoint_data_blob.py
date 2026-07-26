"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelEndpointDataBlob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.blob
    import capo_frauddetector.types.content_type


class ModelEndpointDataBlob(TypedDict, closed=True):
    byte_buffer: NotRequired["capo_frauddetector.types.blob.blob"]
    """<p>The byte buffer of the Amazon SageMaker model endpoint input data blob.</p>"""
    content_type: NotRequired["capo_frauddetector.types.content_type.contentType"]
    """<p>The content type of the Amazon SageMaker model endpoint input data blob. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelEndpointDataBlob) -> dict:
    out: dict = {}
    if "byte_buffer" in value:
        import capo_frauddetector.types.blob

        out["byteBuffer"] = capo_frauddetector.types.blob.serialize_aws_json_1_1(
            value["byte_buffer"]
        )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelEndpointDataBlob:
    out: ModelEndpointDataBlob = {}  # type: ignore[typeddict-item]
    if "byteBuffer" in data:
        import capo_frauddetector.types.blob

        out["byte_buffer"] = capo_frauddetector.types.blob.deserialize_aws_json_1_1(
            data["byteBuffer"]
        )
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    return out
