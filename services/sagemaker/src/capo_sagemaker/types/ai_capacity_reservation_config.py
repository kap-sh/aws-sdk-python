"""Generated from Smithy shape ``com.amazonaws.sagemaker#AICapacityReservationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_capacity_reservation_preference
    import capo_sagemaker.types.ai_ml_reservation_arn_list


class AICapacityReservationConfig(TypedDict, closed=True):
    capacity_reservation_preference: NotRequired[
        "capo_sagemaker.types.ai_capacity_reservation_preference.AICapacityReservationPreference"
    ]
    """<p>The capacity reservation preference. The only valid value is <code>capacity-reservations-only</code>.</p>"""
    ml_reservation_arns: NotRequired[
        "capo_sagemaker.types.ai_ml_reservation_arn_list.AIMlReservationArnList"
    ]
    """<p>The list of ML reservation ARNs to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AICapacityReservationConfig) -> dict:
    out: dict = {}
    if "capacity_reservation_preference" in value:
        import capo_sagemaker.types.ai_capacity_reservation_preference

        out["CapacityReservationPreference"] = (
            capo_sagemaker.types.ai_capacity_reservation_preference.serialize_aws_json_1_1(
                value["capacity_reservation_preference"]
            )
        )
    if "ml_reservation_arns" in value:
        import capo_sagemaker.types.ai_ml_reservation_arn_list

        out["MlReservationArns"] = (
            capo_sagemaker.types.ai_ml_reservation_arn_list.serialize_aws_json_1_1(
                value["ml_reservation_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AICapacityReservationConfig:
    out: AICapacityReservationConfig = {}  # type: ignore[typeddict-item]
    if "CapacityReservationPreference" in data:
        import capo_sagemaker.types.ai_capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            capo_sagemaker.types.ai_capacity_reservation_preference.deserialize_aws_json_1_1(
                data["CapacityReservationPreference"]
            )
        )
    if "MlReservationArns" in data:
        import capo_sagemaker.types.ai_ml_reservation_arn_list

        out["ml_reservation_arns"] = (
            capo_sagemaker.types.ai_ml_reservation_arn_list.deserialize_aws_json_1_1(
                data["MlReservationArns"]
            )
        )
    return out
