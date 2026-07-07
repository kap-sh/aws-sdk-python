"""Generated from Smithy shape ``com.amazonaws.machinelearning#PredictInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.record
    import aws_sdk_machine_learning.types.vip_url


class PredictInput(TypedDict, closed=True):
    ml_model_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>A unique identifier of the <code>MLModel</code>.</p>"""
    record: "aws_sdk_machine_learning.types.record.Record"
    predict_endpoint: "aws_sdk_machine_learning.types.vip_url.VipURL"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    import aws_sdk_machine_learning.types.record

    out["Record"] = aws_sdk_machine_learning.types.record.serialize_aws_json_1_1(
        value["record"]
    )
    out["PredictEndpoint"] = value["predict_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictInput:
    out: PredictInput = {}  # type: ignore[typeddict-item]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    else:
        raise DeserializationError("PredictInput.ml_model_id required")
    if "Record" in data:
        import aws_sdk_machine_learning.types.record

        out["record"] = aws_sdk_machine_learning.types.record.deserialize_aws_json_1_1(
            data["Record"]
        )
    else:
        raise DeserializationError("PredictInput.record required")
    if "PredictEndpoint" in data:
        out["predict_endpoint"] = data["PredictEndpoint"]
    else:
        raise DeserializationError("PredictInput.predict_endpoint required")
    return out
