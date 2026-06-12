"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantCapacityReservationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_reservation_preference
    import aws_sdk_sagemaker.types.ec2_capacity_reservations_list
    import aws_sdk_sagemaker.types.ml_reservation_arn
    import aws_sdk_sagemaker.types.task_count


class ProductionVariantCapacityReservationSummary(TypedDict):
    ml_reservation_arn: NotRequired[
        "aws_sdk_sagemaker.types.ml_reservation_arn.MlReservationArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the ML capacity reservation that SageMaker AI applies when it deploys the endpoint.</p>"""
    capacity_reservation_preference: NotRequired[
        "aws_sdk_sagemaker.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>The option that you chose for the capacity reservation. SageMaker AI supports the following options:</p> <dl> <dt>capacity-reservations-only</dt> <dd> <p>SageMaker AI launches instances only into an ML capacity reservation. If no capacity is available, the instances fail to launch.</p> </dd> </dl>"""
    total_instance_count: NotRequired["aws_sdk_sagemaker.types.task_count.TaskCount"]
    """<p>The number of instances that you allocated to the ML capacity reservation.</p>"""
    available_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.task_count.TaskCount"
    ]
    """<p>The number of instances that are currently available in the ML capacity reservation.</p>"""
    used_by_current_endpoint: NotRequired[
        "aws_sdk_sagemaker.types.task_count.TaskCount"
    ]
    """<p>The number of instances from the ML capacity reservation that are being used by the endpoint.</p>"""
    ec2_capacity_reservations: NotRequired[
        "aws_sdk_sagemaker.types.ec2_capacity_reservations_list.Ec2CapacityReservationsList"
    ]
    """<p>The EC2 capacity reservations that are shared to this ML capacity reservation, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantCapacityReservationSummary) -> dict:
    out: dict = {}
    if "ml_reservation_arn" in value:
        out["MlReservationArn"] = value["ml_reservation_arn"]
    if "capacity_reservation_preference" in value:
        import aws_sdk_sagemaker.types.capacity_reservation_preference

        out["CapacityReservationPreference"] = (
            aws_sdk_sagemaker.types.capacity_reservation_preference.serialize_aws_json_1_1(
                value["capacity_reservation_preference"]
            )
        )
    if "total_instance_count" in value:
        out["TotalInstanceCount"] = value["total_instance_count"]
    if "available_instance_count" in value:
        out["AvailableInstanceCount"] = value["available_instance_count"]
    if "used_by_current_endpoint" in value:
        out["UsedByCurrentEndpoint"] = value["used_by_current_endpoint"]
    if "ec2_capacity_reservations" in value:
        import aws_sdk_sagemaker.types.ec2_capacity_reservations_list

        out["Ec2CapacityReservations"] = (
            aws_sdk_sagemaker.types.ec2_capacity_reservations_list.serialize_aws_json_1_1(
                value["ec2_capacity_reservations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantCapacityReservationSummary:
    out: ProductionVariantCapacityReservationSummary = {}  # type: ignore[typeddict-item]
    if "MlReservationArn" in data:
        out["ml_reservation_arn"] = data["MlReservationArn"]
    if "CapacityReservationPreference" in data:
        import aws_sdk_sagemaker.types.capacity_reservation_preference

        out["capacity_reservation_preference"] = (
            aws_sdk_sagemaker.types.capacity_reservation_preference.deserialize_aws_json_1_1(
                data["CapacityReservationPreference"]
            )
        )
    if "TotalInstanceCount" in data:
        out["total_instance_count"] = data["TotalInstanceCount"]
    if "AvailableInstanceCount" in data:
        out["available_instance_count"] = data["AvailableInstanceCount"]
    if "UsedByCurrentEndpoint" in data:
        out["used_by_current_endpoint"] = data["UsedByCurrentEndpoint"]
    if "Ec2CapacityReservations" in data:
        import aws_sdk_sagemaker.types.ec2_capacity_reservations_list

        out["ec2_capacity_reservations"] = (
            aws_sdk_sagemaker.types.ec2_capacity_reservations_list.deserialize_aws_json_1_1(
                data["Ec2CapacityReservations"]
            )
        )
    return out
