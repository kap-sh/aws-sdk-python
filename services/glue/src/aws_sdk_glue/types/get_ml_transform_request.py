"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTransformRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class GetMLTransformRequest(TypedDict, closed=True):
    transform_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The unique identifier of the transform, generated at the time that the transform was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTransformRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTransformRequest:
    out: GetMLTransformRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError("GetMLTransformRequest.transform_id required")
    return out
