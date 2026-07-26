"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAssignmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.capacity_assignments_list
    import capo_athena.types.capacity_reservation_name


class CapacityAssignmentConfiguration(TypedDict, closed=True):
    capacity_reservation_name: NotRequired[
        "capo_athena.types.capacity_reservation_name.CapacityReservationName"
    ]
    """<p>The name of the reservation that the capacity assignment configuration is for.</p>"""
    capacity_assignments: NotRequired[
        "capo_athena.types.capacity_assignments_list.CapacityAssignmentsList"
    ]
    """<p>The list of assignments that make up the capacity assignment configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAssignmentConfiguration) -> dict:
    out: dict = {}
    if "capacity_reservation_name" in value:
        out["CapacityReservationName"] = value["capacity_reservation_name"]
    if "capacity_assignments" in value:
        import capo_athena.types.capacity_assignments_list

        out["CapacityAssignments"] = (
            capo_athena.types.capacity_assignments_list.serialize_aws_json_1_1(
                value["capacity_assignments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityAssignmentConfiguration:
    out: CapacityAssignmentConfiguration = {}  # type: ignore[typeddict-item]
    if "CapacityReservationName" in data:
        out["capacity_reservation_name"] = data["CapacityReservationName"]
    if "CapacityAssignments" in data:
        import capo_athena.types.capacity_assignments_list

        out["capacity_assignments"] = (
            capo_athena.types.capacity_assignments_list.deserialize_aws_json_1_1(
                data["CapacityAssignments"]
            )
        )
    return out
