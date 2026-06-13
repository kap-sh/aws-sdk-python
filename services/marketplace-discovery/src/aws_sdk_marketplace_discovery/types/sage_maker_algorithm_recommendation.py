"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SageMakerAlgorithmRecommendation``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError


class SageMakerAlgorithmRecommendation(TypedDict):
    recommended_batch_transform_instance_type: "str"
    """<p>The recommended instance type for batch inference.</p>"""
    recommended_realtime_inference_instance_type: NotRequired["str"]
    """<p>The recommended instance type for real-time inference.</p>"""
    recommended_training_instance_type: "str"
    """<p>The recommended instance type for training.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerAlgorithmRecommendation) -> dict:
    out: dict = {}
    out["recommendedBatchTransformInstanceType"] = value[
        "recommended_batch_transform_instance_type"
    ]
    if "recommended_realtime_inference_instance_type" in value:
        out["recommendedRealtimeInferenceInstanceType"] = value[
            "recommended_realtime_inference_instance_type"
        ]
    out["recommendedTrainingInstanceType"] = value["recommended_training_instance_type"]
    return out


def deserialize_json(data: dict) -> SageMakerAlgorithmRecommendation:
    out: SageMakerAlgorithmRecommendation = {}  # type: ignore[typeddict-item]
    if "recommendedBatchTransformInstanceType" in data:
        out["recommended_batch_transform_instance_type"] = data[
            "recommendedBatchTransformInstanceType"
        ]
    else:
        raise DeserializationError(
            "SageMakerAlgorithmRecommendation.recommended_batch_transform_instance_type required"
        )
    if "recommendedRealtimeInferenceInstanceType" in data:
        out["recommended_realtime_inference_instance_type"] = data[
            "recommendedRealtimeInferenceInstanceType"
        ]
    if "recommendedTrainingInstanceType" in data:
        out["recommended_training_instance_type"] = data[
            "recommendedTrainingInstanceType"
        ]
    else:
        raise DeserializationError(
            "SageMakerAlgorithmRecommendation.recommended_training_instance_type required"
        )
    return out
