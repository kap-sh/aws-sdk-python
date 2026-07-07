"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantCapacityReservationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_reservation_preference
    import aws_sdk_sagemaker.types.ml_reservation_arn


class ProductionVariantCapacityReservationConfig(TypedDict, closed=True):
    capacity_reservation_preference: NotRequired[
        "aws_sdk_sagemaker.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>Options that you can choose for the capacity reservation. SageMaker AI supports the following options:</p> <dl> <dt>capacity-reservations-only</dt> <dd> <p>SageMaker AI launches instances only into an ML capacity reservation. If no capacity is available, the instances fail to launch.</p> </dd> </dl>"""
    ml_reservation_arn: NotRequired[
        "aws_sdk_sagemaker.types.ml_reservation_arn.MlReservationArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the ML capacity reservation that SageMaker AI applies when it deploys the endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantCapacityReservationConfig) -> dict:
    out: dict = {}
    if "capacity_reservation_preference" in value:
        import aws_sdk_sagemaker.types.capacity_reservation_preference

        out["CapacityReservationPreference"] = (
            aws_sdk_sagemaker.types.capacity_reservation_preference.serialize_aws_json_1_1(
                value["capacity_reservation_preference"]
            )
        )
    if "ml_reservation_arn" in value:
        out["MlReservationArn"] = value["ml_reservation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantCapacityReservationConfig:
    out: ProductionVariantCapacityReservationConfig = {}  # type: ignore[typeddict-item]
    if "CapacityReservationPreference" in data:
        import aws_sdk_sagemaker.types.capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            aws_sdk_sagemaker.types.capacity_reservation_preference.deserialize_aws_json_1_1(
                data["CapacityReservationPreference"]
            )
        )
    if "MlReservationArn" in data:
        out["ml_reservation_arn"] = data["MlReservationArn"]
    return out
