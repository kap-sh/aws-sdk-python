"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalShiftInResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.applied_status
    import aws_sdk_arc_zonal_shift.types.availability_zone
    import aws_sdk_arc_zonal_shift.types.expiry_time
    import aws_sdk_arc_zonal_shift.types.practice_run_outcome
    import aws_sdk_arc_zonal_shift.types.resource_identifier
    import aws_sdk_arc_zonal_shift.types.shift_type
    import aws_sdk_arc_zonal_shift.types.start_time
    import aws_sdk_arc_zonal_shift.types.zonal_shift_comment
    import aws_sdk_arc_zonal_shift.types.zonal_shift_id


class ZonalShiftInResource(TypedDict, closed=True):
    applied_status: "aws_sdk_arc_zonal_shift.types.applied_status.AppliedStatus"
    r"""<p>The <code>appliedStatus</code> field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The <code>appliedStatus</code> field for a shift that is in progress for a resource can have one of two values: <code>APPLIED</code> or <code>NOT_APPLIED</code>. The zonal shift or autoshift that is currently in effect for the resource has an <code>appliedStatus</code> set to <code>APPLIED</code>.</p> <p>The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts &gt; autoshifts &gt; practice run zonal shifts.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html\">How zonal autoshift and practice runs work</a> in the Amazon Application Recovery Controller Developer Guide.</p>"""
    zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId"
    """<p>The identifier of a zonal shift.</p>"""
    resource_identifier: (
        "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
    )
    r"""<p>The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html\">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html\">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html\">Application Load Balancer</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html\">Network Load Balancer</a> </p> </li> </ul>"""
    away_from: "aws_sdk_arc_zonal_shift.types.availability_zone.AvailabilityZone"
    """<p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the Amazon Web Services Region.</p>"""
    expiry_time: "aws_sdk_arc_zonal_shift.types.expiry_time.ExpiryTime"
    """<p>The expiry time (expiration time) for a customer-initiated zonal shift. A zonal shift is temporary and must be set to expire when you start the zonal shift. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time. </p> <p>When you start a zonal shift, you specify how long you want it to be active, which ARC converts to an expiry time (expiration time). You can cancel a zonal shift when you're ready to restore traffic to the Availability Zone, or just wait for it to expire. Or you can update the zonal shift to specify another length of time to expire in.</p>"""
    start_time: "aws_sdk_arc_zonal_shift.types.start_time.StartTime"
    """<p>The time (UTC) when the zonal shift starts.</p>"""
    comment: "aws_sdk_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
    """<p>A comment that you enter for a customer-initiated zonal shift. Only the latest comment is retained; no comment history is maintained. That is, a new comment overwrites any existing comment string.</p>"""
    shift_type: NotRequired["aws_sdk_arc_zonal_shift.types.shift_type.ShiftType"]
    """<p>Defines the zonal shift type.</p>"""
    practice_run_outcome: NotRequired[
        "aws_sdk_arc_zonal_shift.types.practice_run_outcome.PracticeRunOutcome"
    ]
    r"""<p>The outcome, or end state, returned for a practice run. The following values can be returned:</p> <ul> <li> <p> <b>PENDING:</b> Outcome value when a practice run is in progress.</p> </li> <li> <p> <b>SUCCEEDED:</b> Outcome value when the outcome alarm specified for the practice run configuration does not go into an <code>ALARM</code> state during the practice run, and the practice run was not interrupted before it completed the expected 30 minute zonal shift.</p> </li> <li> <p> <b>INTERRUPTED:</b> Outcome value when the practice run was stopped before the expected 30 minute zonal shift duration, or there was another problem with the practice run that created an inconclusive outcome.</p> </li> <li> <p> <b>FAILED:</b> Outcome value when the outcome alarm specified for the practice run configuration goes into an <code>ALARM</code> state during the practice run, and the practice run was not interrupted before it completed.</p> </li> <li> <p> <b>CAPACITY_CHECK_FAILED:</b> The check for balanced capacity across Availability Zones for your load balancing and Auto Scaling group resources failed.</p> </li> </ul> <p>For more information about practice run outcomes, see <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.configure.html\"> Considerations when you configure zonal autoshift</a> in the Amazon Application Recovery Controller Developer Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZonalShiftInResource) -> dict:
    out: dict = {}
    import aws_sdk_arc_zonal_shift.types.applied_status

    out["appliedStatus"] = aws_sdk_arc_zonal_shift.types.applied_status.serialize_json(
        value["applied_status"]
    )
    out["zonalShiftId"] = value["zonal_shift_id"]
    out["resourceIdentifier"] = value["resource_identifier"]
    out["awayFrom"] = value["away_from"]
    import aws_sdk_arc_zonal_shift.types.expiry_time

    out["expiryTime"] = aws_sdk_arc_zonal_shift.types.expiry_time.serialize_json(
        value["expiry_time"]
    )
    import aws_sdk_arc_zonal_shift.types.start_time

    out["startTime"] = aws_sdk_arc_zonal_shift.types.start_time.serialize_json(
        value["start_time"]
    )
    out["comment"] = value["comment"]
    if "shift_type" in value:
        import aws_sdk_arc_zonal_shift.types.shift_type

        out["shiftType"] = aws_sdk_arc_zonal_shift.types.shift_type.serialize_json(
            value["shift_type"]
        )
    if "practice_run_outcome" in value:
        import aws_sdk_arc_zonal_shift.types.practice_run_outcome

        out["practiceRunOutcome"] = (
            aws_sdk_arc_zonal_shift.types.practice_run_outcome.serialize_json(
                value["practice_run_outcome"]
            )
        )
    return out


def deserialize_json(data: dict) -> ZonalShiftInResource:
    out: ZonalShiftInResource = {}  # type: ignore[typeddict-item]
    if "appliedStatus" in data:
        import aws_sdk_arc_zonal_shift.types.applied_status

        out["applied_status"] = (
            aws_sdk_arc_zonal_shift.types.applied_status.deserialize_json(
                data["appliedStatus"]
            )
        )
    else:
        raise DeserializationError("ZonalShiftInResource.applied_status required")
    if "zonalShiftId" in data:
        out["zonal_shift_id"] = data["zonalShiftId"]
    else:
        raise DeserializationError("ZonalShiftInResource.zonal_shift_id required")
    if "resourceIdentifier" in data:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError("ZonalShiftInResource.resource_identifier required")
    if "awayFrom" in data:
        out["away_from"] = data["awayFrom"]
    else:
        raise DeserializationError("ZonalShiftInResource.away_from required")
    if "expiryTime" in data:
        import aws_sdk_arc_zonal_shift.types.expiry_time

        out["expiry_time"] = aws_sdk_arc_zonal_shift.types.expiry_time.deserialize_json(
            data["expiryTime"]
        )
    else:
        raise DeserializationError("ZonalShiftInResource.expiry_time required")
    if "startTime" in data:
        import aws_sdk_arc_zonal_shift.types.start_time

        out["start_time"] = aws_sdk_arc_zonal_shift.types.start_time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("ZonalShiftInResource.start_time required")
    if "comment" in data:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError("ZonalShiftInResource.comment required")
    if "shiftType" in data:
        import aws_sdk_arc_zonal_shift.types.shift_type

        out["shift_type"] = aws_sdk_arc_zonal_shift.types.shift_type.deserialize_json(
            data["shiftType"]
        )
    if "practiceRunOutcome" in data:
        import aws_sdk_arc_zonal_shift.types.practice_run_outcome

        out["practice_run_outcome"] = (
            aws_sdk_arc_zonal_shift.types.practice_run_outcome.deserialize_json(
                data["practiceRunOutcome"]
            )
        )
    return out
