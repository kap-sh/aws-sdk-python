"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ManagedResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.applied_weights
    import aws_sdk_arc_zonal_shift.types.autoshifts_in_resource
    import aws_sdk_arc_zonal_shift.types.availability_zones
    import aws_sdk_arc_zonal_shift.types.resource_arn
    import aws_sdk_arc_zonal_shift.types.resource_name
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status
    import aws_sdk_arc_zonal_shift.types.zonal_shifts_in_resource


class ManagedResourceSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_arc_zonal_shift.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) for the managed resource.</p>"""
    name: NotRequired["aws_sdk_arc_zonal_shift.types.resource_name.ResourceName"]
    """<p>The name of the managed resource.</p>"""
    availability_zones: (
        "aws_sdk_arc_zonal_shift.types.availability_zones.AvailabilityZones"
    )
    """<p>The Availability Zones that a resource is deployed in.</p>"""
    applied_weights: NotRequired[
        "aws_sdk_arc_zonal_shift.types.applied_weights.AppliedWeights"
    ]
    """<p>A collection of key-value pairs that indicate whether resources are active in Availability Zones or not. The key name is the Availability Zone where the resource is deployed. The value is 1 or 0.</p>"""
    zonal_shifts: NotRequired[
        "aws_sdk_arc_zonal_shift.types.zonal_shifts_in_resource.ZonalShiftsInResource"
    ]
    """<p>An array of the zonal shifts for a resource.</p>"""
    autoshifts: NotRequired[
        "aws_sdk_arc_zonal_shift.types.autoshifts_in_resource.AutoshiftsInResource"
    ]
    """<p>An array of the autoshifts that have been completed for a resource.</p>"""
    zonal_autoshift_status: NotRequired[
        "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    ]
    """<p>The status of autoshift for a resource. When you configure zonal autoshift for a resource, you can set the value of the status to <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    practice_run_status: NotRequired[
        "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus"
    ]
    """<p>This status tracks whether a practice run configuration exists for a resource. When you configure a practice run for a resource so that a practice run configuration exists, ARC sets this value to <code>ENABLED</code>. If a you have not configured a practice run for the resource, or delete a practice run configuration, ARC sets the value to <code>DISABLED</code>.</p> <p>ARC updates this status; you can't set a practice run status to <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedResourceSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_arc_zonal_shift.types.availability_zones

    out["availabilityZones"] = (
        aws_sdk_arc_zonal_shift.types.availability_zones.serialize_json(
            value["availability_zones"]
        )
    )
    if "applied_weights" in value:
        import aws_sdk_arc_zonal_shift.types.applied_weights

        out["appliedWeights"] = (
            aws_sdk_arc_zonal_shift.types.applied_weights.serialize_json(
                value["applied_weights"]
            )
        )
    if "zonal_shifts" in value:
        import aws_sdk_arc_zonal_shift.types.zonal_shifts_in_resource

        out["zonalShifts"] = (
            aws_sdk_arc_zonal_shift.types.zonal_shifts_in_resource.serialize_json(
                value["zonal_shifts"]
            )
        )
    if "autoshifts" in value:
        import aws_sdk_arc_zonal_shift.types.autoshifts_in_resource

        out["autoshifts"] = (
            aws_sdk_arc_zonal_shift.types.autoshifts_in_resource.serialize_json(
                value["autoshifts"]
            )
        )
    if "zonal_autoshift_status" in value:
        import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

        out["zonalAutoshiftStatus"] = (
            aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
                value["zonal_autoshift_status"]
            )
        )
    if "practice_run_status" in value:
        import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

        out["practiceRunStatus"] = (
            aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.serialize_json(
                value["practice_run_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedResourceSummary:
    out: ManagedResourceSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "availabilityZones" in data:
        import aws_sdk_arc_zonal_shift.types.availability_zones

        out["availability_zones"] = (
            aws_sdk_arc_zonal_shift.types.availability_zones.deserialize_json(
                data["availabilityZones"]
            )
        )
    else:
        raise DeserializationError("ManagedResourceSummary.availability_zones required")
    if "appliedWeights" in data:
        import aws_sdk_arc_zonal_shift.types.applied_weights

        out["applied_weights"] = (
            aws_sdk_arc_zonal_shift.types.applied_weights.deserialize_json(
                data["appliedWeights"]
            )
        )
    if "zonalShifts" in data:
        import aws_sdk_arc_zonal_shift.types.zonal_shifts_in_resource

        out["zonal_shifts"] = (
            aws_sdk_arc_zonal_shift.types.zonal_shifts_in_resource.deserialize_json(
                data["zonalShifts"]
            )
        )
    if "autoshifts" in data:
        import aws_sdk_arc_zonal_shift.types.autoshifts_in_resource

        out["autoshifts"] = (
            aws_sdk_arc_zonal_shift.types.autoshifts_in_resource.deserialize_json(
                data["autoshifts"]
            )
        )
    if "zonalAutoshiftStatus" in data:
        import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

        out["zonal_autoshift_status"] = (
            aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.deserialize_json(
                data["zonalAutoshiftStatus"]
            )
        )
    if "practiceRunStatus" in data:
        import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status

        out["practice_run_status"] = (
            aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.deserialize_json(
                data["practiceRunStatus"]
            )
        )
    return out
