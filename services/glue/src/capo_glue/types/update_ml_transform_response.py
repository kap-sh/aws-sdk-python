"""Generated from Smithy shape ``com.amazonaws.glue#UpdateMLTransformResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class UpdateMLTransformResponse(TypedDict, closed=True):
    transform_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique identifier for the transform that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMLTransformResponse) -> dict:
    out: dict = {}
    if "transform_id" in value:
        out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMLTransformResponse:
    out: UpdateMLTransformResponse = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    return out
