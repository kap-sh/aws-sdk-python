"""Generated from Smithy shape ``com.amazonaws.athena#CapacityReservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.allocated_dpus_integer
    import aws_sdk_athena.types.capacity_allocation
    import aws_sdk_athena.types.capacity_reservation_name
    import aws_sdk_athena.types.capacity_reservation_status
    import aws_sdk_athena.types.target_dpus_integer
    import aws_sdk_athena.types.timestamp


class CapacityReservation(TypedDict, closed=True):
    name: "aws_sdk_athena.types.capacity_reservation_name.CapacityReservationName"
    """<p>The name of the capacity reservation.</p>"""
    status: "aws_sdk_athena.types.capacity_reservation_status.CapacityReservationStatus"
    """<p>The status of the capacity reservation.</p>"""
    target_dpus: "aws_sdk_athena.types.target_dpus_integer.TargetDpusInteger"
    """<p>The number of data processing units requested.</p>"""
    allocated_dpus: "aws_sdk_athena.types.allocated_dpus_integer.AllocatedDpusInteger"
    """<p>The number of data processing units currently allocated.</p>"""
    last_allocation: NotRequired[
        "aws_sdk_athena.types.capacity_allocation.CapacityAllocation"
    ]
    last_successful_allocation_time: NotRequired[
        "aws_sdk_athena.types.timestamp.Timestamp"
    ]
    """<p>The time of the most recent capacity allocation that succeeded.</p>"""
    creation_time: "aws_sdk_athena.types.timestamp.Timestamp"
    """<p>The time in UTC epoch millis when the capacity reservation was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservation) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_athena.types.capacity_reservation_status

    out["Status"] = (
        aws_sdk_athena.types.capacity_reservation_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    out["TargetDpus"] = value["target_dpus"]
    out["AllocatedDpus"] = value["allocated_dpus"]
    if "last_allocation" in value:
        import aws_sdk_athena.types.capacity_allocation

        out["LastAllocation"] = (
            aws_sdk_athena.types.capacity_allocation.serialize_aws_json_1_1(
                value["last_allocation"]
            )
        )
    if "last_successful_allocation_time" in value:
        import aws_sdk_athena.types.timestamp

        out["LastSuccessfulAllocationTime"] = (
            aws_sdk_athena.types.timestamp.serialize_aws_json_1_1(
                value["last_successful_allocation_time"]
            )
        )
    import aws_sdk_athena.types.timestamp

    out["CreationTime"] = aws_sdk_athena.types.timestamp.serialize_aws_json_1_1(
        value["creation_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityReservation:
    out: CapacityReservation = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CapacityReservation.name required")
    if "Status" in data:
        import aws_sdk_athena.types.capacity_reservation_status

        out["status"] = (
            aws_sdk_athena.types.capacity_reservation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CapacityReservation.status required")
    if "TargetDpus" in data:
        out["target_dpus"] = data["TargetDpus"]
    else:
        raise DeserializationError("CapacityReservation.target_dpus required")
    if "AllocatedDpus" in data:
        out["allocated_dpus"] = data["AllocatedDpus"]
    else:
        raise DeserializationError("CapacityReservation.allocated_dpus required")
    if "LastAllocation" in data:
        import aws_sdk_athena.types.capacity_allocation

        out["last_allocation"] = (
            aws_sdk_athena.types.capacity_allocation.deserialize_aws_json_1_1(
                data["LastAllocation"]
            )
        )
    if "LastSuccessfulAllocationTime" in data:
        import aws_sdk_athena.types.timestamp

        out["last_successful_allocation_time"] = (
            aws_sdk_athena.types.timestamp.deserialize_aws_json_1_1(
                data["LastSuccessfulAllocationTime"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_athena.types.timestamp

        out["creation_time"] = aws_sdk_athena.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    else:
        raise DeserializationError("CapacityReservation.creation_time required")
    return out
