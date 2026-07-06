"""Generated from Smithy shape ``com.amazonaws.glue#CreateMLTransformResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class CreateMLTransformResponse(TypedDict, closed=True):
    transform_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>A unique identifier that is generated for the transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMLTransformResponse) -> dict:
    out: dict = {}
    if "transform_id" in value:
        out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMLTransformResponse:
    out: CreateMLTransformResponse = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    return out
