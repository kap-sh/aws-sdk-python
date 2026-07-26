"""Generated from Smithy shape ``com.amazonaws.finspacedata#ChangesetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.change_type
    import capo_finspace_data.types.changeset_arn
    import capo_finspace_data.types.changeset_error_info
    import capo_finspace_data.types.changeset_id
    import capo_finspace_data.types.dataset_id
    import capo_finspace_data.types.format_params
    import capo_finspace_data.types.ingestion_status
    import capo_finspace_data.types.source_params
    import capo_finspace_data.types.timestamp_epoch


class ChangesetSummary(TypedDict, closed=True):
    changeset_id: NotRequired["capo_finspace_data.types.changeset_id.ChangesetId"]
    """<p>The unique identifier for a Changeset.</p>"""
    changeset_arn: NotRequired["capo_finspace_data.types.changeset_arn.ChangesetArn"]
    """<p>The ARN identifier of the Changeset.</p>"""
    dataset_id: NotRequired["capo_finspace_data.types.dataset_id.DatasetId"]
    """<p>The unique identifier for the FinSpace Dataset in which the Changeset is created.</p>"""
    change_type: NotRequired["capo_finspace_data.types.change_type.ChangeType"]
    """<p>Type that indicates how a Changeset is applied to a Dataset.</p> <ul> <li> <p> <code>REPLACE</code> – Changeset is considered as a replacement to all prior loaded Changesets.</p> </li> <li> <p> <code>APPEND</code> – Changeset is considered as an addition to the end of all prior loaded Changesets.</p> </li> <li> <p> <code>MODIFY</code> – Changeset is considered as a replacement to a specific prior ingested Changeset.</p> </li> </ul>"""
    source_params: NotRequired["capo_finspace_data.types.source_params.SourceParams"]
    """<p>Options that define the location of the data being ingested.</p>"""
    format_params: NotRequired["capo_finspace_data.types.format_params.FormatParams"]
    """<p>Options that define the structure of the source file(s).</p>"""
    create_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The timestamp at which the Changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    status: NotRequired["capo_finspace_data.types.ingestion_status.IngestionStatus"]
    """<p>Status of the Changeset ingestion.</p> <ul> <li> <p> <code>PENDING</code> – Changeset is pending creation.</p> </li> <li> <p> <code>FAILED</code> – Changeset creation has failed.</p> </li> <li> <p> <code>SUCCESS</code> – Changeset creation has succeeded.</p> </li> <li> <p> <code>RUNNING</code> – Changeset creation is running.</p> </li> <li> <p> <code>STOP_REQUESTED</code> – User requested Changeset creation to stop.</p> </li> </ul>"""
    error_info: NotRequired[
        "capo_finspace_data.types.changeset_error_info.ChangesetErrorInfo"
    ]
    """<p>The structure with error messages.</p>"""
    active_until_timestamp: NotRequired[
        "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    ]
    """<p>Time until which the Changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    active_from_timestamp: NotRequired[
        "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    ]
    """<p>Beginning time from which the Changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    updates_changeset_id: NotRequired[
        "capo_finspace_data.types.changeset_id.ChangesetId"
    ]
    """<p>The unique identifier of the Changeset that is updated.</p>"""
    updated_by_changeset_id: NotRequired[
        "capo_finspace_data.types.changeset_id.ChangesetId"
    ]
    """<p>The unique identifier of the updated Changeset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangesetSummary) -> dict:
    out: dict = {}
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "changeset_arn" in value:
        out["changesetArn"] = value["changeset_arn"]
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "change_type" in value:
        import capo_finspace_data.types.change_type

        out["changeType"] = capo_finspace_data.types.change_type.serialize_json(
            value["change_type"]
        )
    if "source_params" in value:
        import capo_finspace_data.types.source_params

        out["sourceParams"] = capo_finspace_data.types.source_params.serialize_json(
            value["source_params"]
        )
    if "format_params" in value:
        import capo_finspace_data.types.format_params

        out["formatParams"] = capo_finspace_data.types.format_params.serialize_json(
            value["format_params"]
        )
    out["createTime"] = value.get("create_time", 0)
    if "status" in value:
        import capo_finspace_data.types.ingestion_status

        out["status"] = capo_finspace_data.types.ingestion_status.serialize_json(
            value["status"]
        )
    if "error_info" in value:
        import capo_finspace_data.types.changeset_error_info

        out["errorInfo"] = capo_finspace_data.types.changeset_error_info.serialize_json(
            value["error_info"]
        )
    if "active_until_timestamp" in value:
        out["activeUntilTimestamp"] = value["active_until_timestamp"]
    if "active_from_timestamp" in value:
        out["activeFromTimestamp"] = value["active_from_timestamp"]
    if "updates_changeset_id" in value:
        out["updatesChangesetId"] = value["updates_changeset_id"]
    if "updated_by_changeset_id" in value:
        out["updatedByChangesetId"] = value["updated_by_changeset_id"]
    return out


def deserialize_json(data: dict) -> ChangesetSummary:
    out: ChangesetSummary = {}  # type: ignore[typeddict-item]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "changesetArn" in data:
        out["changeset_arn"] = data["changesetArn"]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    if "changeType" in data:
        import capo_finspace_data.types.change_type

        out["change_type"] = capo_finspace_data.types.change_type.deserialize_json(
            data["changeType"]
        )
    if "sourceParams" in data:
        import capo_finspace_data.types.source_params

        out["source_params"] = capo_finspace_data.types.source_params.deserialize_json(
            data["sourceParams"]
        )
    if "formatParams" in data:
        import capo_finspace_data.types.format_params

        out["format_params"] = capo_finspace_data.types.format_params.deserialize_json(
            data["formatParams"]
        )
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = 0
    if "status" in data:
        import capo_finspace_data.types.ingestion_status

        out["status"] = capo_finspace_data.types.ingestion_status.deserialize_json(
            data["status"]
        )
    if "errorInfo" in data:
        import capo_finspace_data.types.changeset_error_info

        out["error_info"] = (
            capo_finspace_data.types.changeset_error_info.deserialize_json(
                data["errorInfo"]
            )
        )
    if "activeUntilTimestamp" in data:
        out["active_until_timestamp"] = data["activeUntilTimestamp"]
    if "activeFromTimestamp" in data:
        out["active_from_timestamp"] = data["activeFromTimestamp"]
    if "updatesChangesetId" in data:
        out["updates_changeset_id"] = data["updatesChangesetId"]
    if "updatedByChangesetId" in data:
        out["updated_by_changeset_id"] = data["updatedByChangesetId"]
    return out
