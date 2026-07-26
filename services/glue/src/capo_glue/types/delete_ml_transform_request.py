"""Generated from Smithy shape ``com.amazonaws.glue#DeleteMLTransformRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class DeleteMLTransformRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the transform to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMLTransformRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMLTransformRequest:
    out: DeleteMLTransformRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError("DeleteMLTransformRequest.transform_id required")
    return out
