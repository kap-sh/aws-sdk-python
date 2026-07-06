"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CapacityReservationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.capacity_reservation_preference_enum
    import aws_sdk_workspaces_instances.types.capacity_reservation_target


class CapacityReservationSpecification(TypedDict, closed=True):
    capacity_reservation_preference: NotRequired[
        "aws_sdk_workspaces_instances.types.capacity_reservation_preference_enum.CapacityReservationPreferenceEnum"
    ]
    """<p>Preference for using capacity reservation.</p>"""
    capacity_reservation_target: NotRequired[
        "aws_sdk_workspaces_instances.types.capacity_reservation_target.CapacityReservationTarget"
    ]
    """<p>Specific capacity reservation target.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityReservationSpecification) -> dict:
    out: dict = {}
    if "capacity_reservation_preference" in value:
        import aws_sdk_workspaces_instances.types.capacity_reservation_preference_enum

        out["CapacityReservationPreference"] = (
            aws_sdk_workspaces_instances.types.capacity_reservation_preference_enum.serialize_aws_json_1_0(
                value["capacity_reservation_preference"]
            )
        )
    if "capacity_reservation_target" in value:
        import aws_sdk_workspaces_instances.types.capacity_reservation_target

        out["CapacityReservationTarget"] = (
            aws_sdk_workspaces_instances.types.capacity_reservation_target.serialize_aws_json_1_0(
                value["capacity_reservation_target"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityReservationSpecification:
    out: CapacityReservationSpecification = {}  # type: ignore[typeddict-item]
    if "CapacityReservationPreference" in data:
        import aws_sdk_workspaces_instances.types.capacity_reservation_preference_enum

        out["capacity_reservation_preference"] = (
            aws_sdk_workspaces_instances.types.capacity_reservation_preference_enum.deserialize_aws_json_1_0(
                data["CapacityReservationPreference"]
            )
        )
    if "CapacityReservationTarget" in data:
        import aws_sdk_workspaces_instances.types.capacity_reservation_target

        out["capacity_reservation_target"] = (
            aws_sdk_workspaces_instances.types.capacity_reservation_target.deserialize_aws_json_1_0(
                data["CapacityReservationTarget"]
            )
        )
    return out
