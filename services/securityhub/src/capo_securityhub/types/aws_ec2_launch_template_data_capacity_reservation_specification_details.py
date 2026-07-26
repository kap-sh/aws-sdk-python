"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_capacity_reservation_target_details
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails(
    TypedDict, closed=True
):
    capacity_reservation_preference: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates the instance's Capacity Reservation preferences. If equal to <code>open</code>, the instance can run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone). If equal to <code>none</code>, the instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity. </p>"""
    capacity_reservation_target: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_capacity_reservation_target_details.AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails"
    ]
    """<p> Specifies a target Capacity Reservation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails,
) -> dict:
    out: dict = {}
    if "capacity_reservation_preference" in value:
        out["CapacityReservationPreference"] = value["capacity_reservation_preference"]
    if "capacity_reservation_target" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_capacity_reservation_target_details

        out["CapacityReservationTarget"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_capacity_reservation_target_details.serialize_json(
                value["capacity_reservation_target"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails:
    out: AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails = {}  # type: ignore[typeddict-item]
    if "CapacityReservationPreference" in data:
        out["capacity_reservation_preference"] = data["CapacityReservationPreference"]
    if "CapacityReservationTarget" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_capacity_reservation_target_details

        out["capacity_reservation_target"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_capacity_reservation_target_details.deserialize_json(
                data["CapacityReservationTarget"]
            )
        )
    return out
