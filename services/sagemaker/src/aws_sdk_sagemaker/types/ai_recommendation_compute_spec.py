"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationComputeSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_capacity_reservation_config
    import aws_sdk_sagemaker.types.ai_recommendation_instance_type_list


class AIRecommendationComputeSpec(TypedDict, closed=True):
    instance_types: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_instance_type_list.AIRecommendationInstanceTypeList"
    ]
    """<p>The list of instance types to consider for recommendations. You can specify up to 3 instance types.</p>"""
    capacity_reservation_config: NotRequired[
        "aws_sdk_sagemaker.types.ai_capacity_reservation_config.AICapacityReservationConfig"
    ]
    """<p>The capacity reservation configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationComputeSpec) -> dict:
    out: dict = {}
    if "instance_types" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_instance_type_list

        out["InstanceTypes"] = (
            aws_sdk_sagemaker.types.ai_recommendation_instance_type_list.serialize_aws_json_1_1(
                value["instance_types"]
            )
        )
    if "capacity_reservation_config" in value:
        import aws_sdk_sagemaker.types.ai_capacity_reservation_config

        out["CapacityReservationConfig"] = (
            aws_sdk_sagemaker.types.ai_capacity_reservation_config.serialize_aws_json_1_1(
                value["capacity_reservation_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationComputeSpec:
    out: AIRecommendationComputeSpec = {}  # type: ignore[typeddict-item]
    if "InstanceTypes" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_instance_type_list

        out["instance_types"] = (
            aws_sdk_sagemaker.types.ai_recommendation_instance_type_list.deserialize_aws_json_1_1(
                data["InstanceTypes"]
            )
        )
    if "CapacityReservationConfig" in data:
        import aws_sdk_sagemaker.types.ai_capacity_reservation_config

        out["capacity_reservation_config"] = (
            aws_sdk_sagemaker.types.ai_capacity_reservation_config.deserialize_aws_json_1_1(
                data["CapacityReservationConfig"]
            )
        )
    return out
