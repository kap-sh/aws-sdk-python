"""Generated from Smithy shape ``com.amazonaws.comprehend#StopTrainingEntityRecognizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_arn


class StopTrainingEntityRecognizerRequest(TypedDict):
    entity_recognizer_arn: (
        "aws_sdk_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
    )
    """<p>The Amazon Resource Name (ARN) that identifies the entity recognizer currently being trained.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTrainingEntityRecognizerRequest) -> dict:
    out: dict = {}
    out["EntityRecognizerArn"] = value["entity_recognizer_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTrainingEntityRecognizerRequest:
    out: StopTrainingEntityRecognizerRequest = {}  # type: ignore[typeddict-item]
    if "EntityRecognizerArn" in data:
        out["entity_recognizer_arn"] = data["EntityRecognizerArn"]
    else:
        raise DeserializationError(
            "StopTrainingEntityRecognizerRequest.entity_recognizer_arn required"
        )
    return out
