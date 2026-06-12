"""Generated from Smithy shape ``com.amazonaws.glue#DeleteMLTransformResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class DeleteMLTransformResponse(TypedDict):
    transform_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique identifier of the transform that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMLTransformResponse) -> dict:
    out: dict = {}
    if "transform_id" in value:
        out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMLTransformResponse:
    out: DeleteMLTransformResponse = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    return out
