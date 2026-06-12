"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAssignmentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.capacity_assignments_list
    import aws_sdk_athena.types.capacity_reservation_name


class CapacityAssignmentConfiguration(TypedDict):
    capacity_reservation_name: NotRequired[
        "aws_sdk_athena.types.capacity_reservation_name.CapacityReservationName"
    ]
    """<p>The name of the reservation that the capacity assignment configuration is for.</p>"""
    capacity_assignments: NotRequired[
        "aws_sdk_athena.types.capacity_assignments_list.CapacityAssignmentsList"
    ]
    """<p>The list of assignments that make up the capacity assignment configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAssignmentConfiguration) -> dict:
    out: dict = {}
    if "capacity_reservation_name" in value:
        out["CapacityReservationName"] = value["capacity_reservation_name"]
    if "capacity_assignments" in value:
        import aws_sdk_athena.types.capacity_assignments_list

        out["CapacityAssignments"] = (
            aws_sdk_athena.types.capacity_assignments_list.serialize_aws_json_1_1(
                value["capacity_assignments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityAssignmentConfiguration:
    out: CapacityAssignmentConfiguration = {}  # type: ignore[typeddict-item]
    if "CapacityReservationName" in data:
        out["capacity_reservation_name"] = data["CapacityReservationName"]
    if "CapacityAssignments" in data:
        import aws_sdk_athena.types.capacity_assignments_list

        out["capacity_assignments"] = (
            aws_sdk_athena.types.capacity_assignments_list.deserialize_aws_json_1_1(
                data["CapacityAssignments"]
            )
        )
    return out
