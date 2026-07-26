"""Generated from Smithy shape ``com.amazonaws.frauddetector#Model``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_type_enum
    import capo_frauddetector.types.string
    import capo_frauddetector.types.time


class Model(TypedDict, closed=True):
    model_id: NotRequired["capo_frauddetector.types.model_identifier.modelIdentifier"]
    """<p>The model ID.</p>"""
    model_type: NotRequired["capo_frauddetector.types.model_type_enum.ModelTypeEnum"]
    """<p>The model type.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The model description.</p>"""
    event_type_name: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The name of the event type.</p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the model was created.</p>"""
    last_updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of last time the model was updated.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The ARN of the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Model) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "model_type" in value:
        import capo_frauddetector.types.model_type_enum

        out["modelType"] = (
            capo_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
                value["model_type"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Model:
    out: Model = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "modelType" in data:
        import capo_frauddetector.types.model_type_enum

        out["model_type"] = (
            capo_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
