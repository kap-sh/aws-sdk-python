"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails(
    TypedDict, closed=True
):
    capacity_reservation_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the Capacity Reservation in which to run the instance. </p>"""
    capacity_reservation_resource_group_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the Capacity Reservation resource group in which to run the instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails,
) -> dict:
    out: dict = {}
    if "capacity_reservation_id" in value:
        out["CapacityReservationId"] = value["capacity_reservation_id"]
    if "capacity_reservation_resource_group_arn" in value:
        out["CapacityReservationResourceGroupArn"] = value[
            "capacity_reservation_resource_group_arn"
        ]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails:
    out: AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails = {}  # type: ignore[typeddict-item]
    if "CapacityReservationId" in data:
        out["capacity_reservation_id"] = data["CapacityReservationId"]
    if "CapacityReservationResourceGroupArn" in data:
        out["capacity_reservation_resource_group_arn"] = data[
            "CapacityReservationResourceGroupArn"
        ]
    return out
