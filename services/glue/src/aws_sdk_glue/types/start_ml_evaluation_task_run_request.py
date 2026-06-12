"""Generated from Smithy shape ``com.amazonaws.glue#StartMLEvaluationTaskRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class StartMLEvaluationTaskRunRequest(TypedDict):
    transform_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMLEvaluationTaskRunRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMLEvaluationTaskRunRequest:
    out: StartMLEvaluationTaskRunRequest = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    else:
        raise DeserializationError(
            "StartMLEvaluationTaskRunRequest.transform_id required"
        )
    return out
