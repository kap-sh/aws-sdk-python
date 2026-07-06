"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceFinderEnablement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.cloud_trail_arn
    import aws_sdk_auditmanager.types.error_message
    import aws_sdk_auditmanager.types.evidence_finder_backfill_status
    import aws_sdk_auditmanager.types.evidence_finder_enablement_status


class EvidenceFinderEnablement(TypedDict, closed=True):
    event_data_store_arn: NotRequired[
        "aws_sdk_auditmanager.types.cloud_trail_arn.CloudTrailArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudTrail Lake event data store that’s used by evidence finder. The event data store is the lake of evidence data that evidence finder runs queries against.</p>"""
    enablement_status: NotRequired[
        "aws_sdk_auditmanager.types.evidence_finder_enablement_status.EvidenceFinderEnablementStatus"
    ]
    """<p>The current status of the evidence finder feature and the related event data store. </p> <ul> <li> <p> <code>ENABLE_IN_PROGRESS</code> means that you requested to enable evidence finder. An event data store is currently being created to support evidence finder queries.</p> </li> <li> <p> <code>ENABLED</code> means that an event data store was successfully created and evidence finder is enabled. We recommend that you wait 7 days until the event data store is backfilled with your past two years’ worth of evidence data. You can use evidence finder in the meantime, but not all data might be available until the backfill is complete.</p> </li> <li> <p> <code>DISABLE_IN_PROGRESS</code> means that you requested to disable evidence finder, and your request is pending the deletion of the event data store.</p> </li> <li> <p> <code>DISABLED</code> means that you have permanently disabled evidence finder and the event data store has been deleted. You can't re-enable evidence finder after this point.</p> </li> </ul>"""
    backfill_status: NotRequired[
        "aws_sdk_auditmanager.types.evidence_finder_backfill_status.EvidenceFinderBackfillStatus"
    ]
    """<p>The current status of the evidence data backfill process. </p> <p>The backfill starts after you enable evidence finder. During this task, Audit Manager populates an event data store with your past two years’ worth of evidence data so that your evidence can be queried.</p> <ul> <li> <p> <code>NOT_STARTED</code> means that the backfill hasn’t started yet. </p> </li> <li> <p> <code>IN_PROGRESS</code> means that the backfill is in progress. This can take up to 7 days to complete, depending on the amount of evidence data. </p> </li> <li> <p> <code>COMPLETED</code> means that the backfill is complete. All of your past evidence is now queryable. </p> </li> </ul>"""
    error: NotRequired["aws_sdk_auditmanager.types.error_message.ErrorMessage"]
    """<p>Represents any errors that occurred when enabling or disabling evidence finder. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceFinderEnablement) -> dict:
    out: dict = {}
    if "event_data_store_arn" in value:
        out["eventDataStoreArn"] = value["event_data_store_arn"]
    if "enablement_status" in value:
        import aws_sdk_auditmanager.types.evidence_finder_enablement_status

        out["enablementStatus"] = (
            aws_sdk_auditmanager.types.evidence_finder_enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    if "backfill_status" in value:
        import aws_sdk_auditmanager.types.evidence_finder_backfill_status

        out["backfillStatus"] = (
            aws_sdk_auditmanager.types.evidence_finder_backfill_status.serialize_json(
                value["backfill_status"]
            )
        )
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> EvidenceFinderEnablement:
    out: EvidenceFinderEnablement = {}  # type: ignore[typeddict-item]
    if "eventDataStoreArn" in data:
        out["event_data_store_arn"] = data["eventDataStoreArn"]
    if "enablementStatus" in data:
        import aws_sdk_auditmanager.types.evidence_finder_enablement_status

        out["enablement_status"] = (
            aws_sdk_auditmanager.types.evidence_finder_enablement_status.deserialize_json(
                data["enablementStatus"]
            )
        )
    if "backfillStatus" in data:
        import aws_sdk_auditmanager.types.evidence_finder_backfill_status

        out["backfill_status"] = (
            aws_sdk_auditmanager.types.evidence_finder_backfill_status.deserialize_json(
                data["backfillStatus"]
            )
        )
    if "error" in data:
        out["error"] = data["error"]
    return out
