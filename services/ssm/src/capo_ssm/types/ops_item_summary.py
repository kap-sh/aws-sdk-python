"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.ops_item_category
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_operational_data
    import capo_ssm.types.ops_item_priority
    import capo_ssm.types.ops_item_severity
    import capo_ssm.types.ops_item_source
    import capo_ssm.types.ops_item_status
    import capo_ssm.types.ops_item_title
    import capo_ssm.types.ops_item_type
    import capo_ssm.types.string


class OpsItemSummary(TypedDict, closed=True):
    created_by: NotRequired["capo_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.</p>"""
    created_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was created.</p>"""
    last_modified_by: NotRequired["capo_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.</p>"""
    last_modified_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was last updated.</p>"""
    priority: NotRequired["capo_ssm.types.ops_item_priority.OpsItemPriority"]
    """<p>The importance of this OpsItem in relation to other OpsItems in the system.</p>"""
    source: NotRequired["capo_ssm.types.ops_item_source.OpsItemSource"]
    """<p>The impacted Amazon Web Services resource.</p>"""
    status: NotRequired["capo_ssm.types.ops_item_status.OpsItemStatus"]
    """<p>The OpsItem status.</p>"""
    ops_item_id: NotRequired["capo_ssm.types.ops_item_id.OpsItemId"]
    """<p>The ID of the OpsItem.</p>"""
    title: NotRequired["capo_ssm.types.ops_item_title.OpsItemTitle"]
    """<p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>"""
    operational_data: NotRequired[
        "capo_ssm.types.ops_item_operational_data.OpsItemOperationalData"
    ]
    """<p>Operational data is custom data that provides useful reference details about the OpsItem. </p>"""
    category: NotRequired["capo_ssm.types.ops_item_category.OpsItemCategory"]
    """<p>A list of OpsItems by category.</p>"""
    severity: NotRequired["capo_ssm.types.ops_item_severity.OpsItemSeverity"]
    """<p>A list of OpsItems by severity.</p>"""
    ops_item_type: NotRequired["capo_ssm.types.ops_item_type.OpsItemType"]
    """<p>The type of OpsItem. Systems Manager supports the following types of OpsItems:</p> <ul> <li> <p> <code>/aws/issue</code> </p> <p>This type of OpsItem is used for default OpsItems created by OpsCenter. </p> </li> <li> <p> <code>/aws/changerequest</code> </p> <p>This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests. </p> </li> <li> <p> <code>/aws/insight</code> </p> <p>This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems. </p> </li> </ul>"""
    actual_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow started. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    actual_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow ended. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemSummary) -> dict:
    out: dict = {}
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "created_time" in value:
        import capo_ssm.types.date_time

        out["CreatedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_time" in value:
        import capo_ssm.types.date_time

        out["LastModifiedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "source" in value:
        out["Source"] = value["source"]
    if "status" in value:
        import capo_ssm.types.ops_item_status

        out["Status"] = capo_ssm.types.ops_item_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "operational_data" in value:
        import capo_ssm.types.ops_item_operational_data

        out["OperationalData"] = (
            capo_ssm.types.ops_item_operational_data.serialize_aws_json_1_1(
                value["operational_data"]
            )
        )
    if "category" in value:
        out["Category"] = value["category"]
    if "severity" in value:
        out["Severity"] = value["severity"]
    if "ops_item_type" in value:
        out["OpsItemType"] = value["ops_item_type"]
    if "actual_start_time" in value:
        import capo_ssm.types.date_time

        out["ActualStartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["actual_start_time"]
        )
    if "actual_end_time" in value:
        import capo_ssm.types.date_time

        out["ActualEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["actual_end_time"]
        )
    if "planned_start_time" in value:
        import capo_ssm.types.date_time

        out["PlannedStartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["planned_start_time"]
        )
    if "planned_end_time" in value:
        import capo_ssm.types.date_time

        out["PlannedEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["planned_end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemSummary:
    out: OpsItemSummary = {}  # type: ignore[typeddict-item]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("CreatedTime") is not None:
        import capo_ssm.types.date_time

        out["created_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedTime") is not None:
        import capo_ssm.types.date_time

        out["last_modified_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
        )
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("Status") is not None:
        import capo_ssm.types.ops_item_status

        out["status"] = capo_ssm.types.ops_item_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("OperationalData") is not None:
        import capo_ssm.types.ops_item_operational_data

        out["operational_data"] = (
            capo_ssm.types.ops_item_operational_data.deserialize_aws_json_1_1(
                data["OperationalData"]
            )
        )
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("Severity") is not None:
        out["severity"] = data["Severity"]
    if data.get("OpsItemType") is not None:
        out["ops_item_type"] = data["OpsItemType"]
    if data.get("ActualStartTime") is not None:
        import capo_ssm.types.date_time

        out["actual_start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ActualStartTime"]
        )
    if data.get("ActualEndTime") is not None:
        import capo_ssm.types.date_time

        out["actual_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ActualEndTime"]
        )
    if data.get("PlannedStartTime") is not None:
        import capo_ssm.types.date_time

        out["planned_start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["PlannedStartTime"]
        )
    if data.get("PlannedEndTime") is not None:
        import capo_ssm.types.date_time

        out["planned_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["PlannedEndTime"]
        )
    return out
