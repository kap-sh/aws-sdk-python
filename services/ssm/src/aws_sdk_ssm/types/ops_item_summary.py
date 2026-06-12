"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.ops_item_category
    import aws_sdk_ssm.types.ops_item_id
    import aws_sdk_ssm.types.ops_item_operational_data
    import aws_sdk_ssm.types.ops_item_priority
    import aws_sdk_ssm.types.ops_item_severity
    import aws_sdk_ssm.types.ops_item_source
    import aws_sdk_ssm.types.ops_item_status
    import aws_sdk_ssm.types.ops_item_title
    import aws_sdk_ssm.types.ops_item_type
    import aws_sdk_ssm.types.string


class OpsItemSummary(TypedDict):
    created_by: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.</p>"""
    created_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was created.</p>"""
    last_modified_by: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.</p>"""
    last_modified_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was last updated.</p>"""
    priority: NotRequired["aws_sdk_ssm.types.ops_item_priority.OpsItemPriority"]
    """<p>The importance of this OpsItem in relation to other OpsItems in the system.</p>"""
    source: NotRequired["aws_sdk_ssm.types.ops_item_source.OpsItemSource"]
    """<p>The impacted Amazon Web Services resource.</p>"""
    status: NotRequired["aws_sdk_ssm.types.ops_item_status.OpsItemStatus"]
    """<p>The OpsItem status.</p>"""
    ops_item_id: NotRequired["aws_sdk_ssm.types.ops_item_id.OpsItemId"]
    """<p>The ID of the OpsItem.</p>"""
    title: NotRequired["aws_sdk_ssm.types.ops_item_title.OpsItemTitle"]
    """<p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>"""
    operational_data: NotRequired[
        "aws_sdk_ssm.types.ops_item_operational_data.OpsItemOperationalData"
    ]
    """<p>Operational data is custom data that provides useful reference details about the OpsItem. </p>"""
    category: NotRequired["aws_sdk_ssm.types.ops_item_category.OpsItemCategory"]
    """<p>A list of OpsItems by category.</p>"""
    severity: NotRequired["aws_sdk_ssm.types.ops_item_severity.OpsItemSeverity"]
    """<p>A list of OpsItems by severity.</p>"""
    ops_item_type: NotRequired["aws_sdk_ssm.types.ops_item_type.OpsItemType"]
    """<p>The type of OpsItem. Systems Manager supports the following types of OpsItems:</p> <ul> <li> <p> <code>/aws/issue</code> </p> <p>This type of OpsItem is used for default OpsItems created by OpsCenter. </p> </li> <li> <p> <code>/aws/changerequest</code> </p> <p>This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests. </p> </li> <li> <p> <code>/aws/insight</code> </p> <p>This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems. </p> </li> </ul>"""
    actual_start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow started. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    actual_end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow ended. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemSummary) -> dict:
    out: dict = {}
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "created_time" in value:
        import aws_sdk_ssm.types.date_time

        out["CreatedTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_time" in value:
        import aws_sdk_ssm.types.date_time

        out["LastModifiedTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "source" in value:
        out["Source"] = value["source"]
    if "status" in value:
        import aws_sdk_ssm.types.ops_item_status

        out["Status"] = aws_sdk_ssm.types.ops_item_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "operational_data" in value:
        import aws_sdk_ssm.types.ops_item_operational_data

        out["OperationalData"] = (
            aws_sdk_ssm.types.ops_item_operational_data.serialize_aws_json_1_1(
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
        import aws_sdk_ssm.types.date_time

        out["ActualStartTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["actual_start_time"]
        )
    if "actual_end_time" in value:
        import aws_sdk_ssm.types.date_time

        out["ActualEndTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["actual_end_time"]
        )
    if "planned_start_time" in value:
        import aws_sdk_ssm.types.date_time

        out["PlannedStartTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["planned_start_time"]
        )
    if "planned_end_time" in value:
        import aws_sdk_ssm.types.date_time

        out["PlannedEndTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["planned_end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemSummary:
    out: OpsItemSummary = {}  # type: ignore[typeddict-item]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreatedTime" in data:
        import aws_sdk_ssm.types.date_time

        out["created_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedTime" in data:
        import aws_sdk_ssm.types.date_time

        out["last_modified_time"] = (
            aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "Status" in data:
        import aws_sdk_ssm.types.ops_item_status

        out["status"] = aws_sdk_ssm.types.ops_item_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "OperationalData" in data:
        import aws_sdk_ssm.types.ops_item_operational_data

        out["operational_data"] = (
            aws_sdk_ssm.types.ops_item_operational_data.deserialize_aws_json_1_1(
                data["OperationalData"]
            )
        )
    if "Category" in data:
        out["category"] = data["Category"]
    if "Severity" in data:
        out["severity"] = data["Severity"]
    if "OpsItemType" in data:
        out["ops_item_type"] = data["OpsItemType"]
    if "ActualStartTime" in data:
        import aws_sdk_ssm.types.date_time

        out["actual_start_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ActualStartTime"]
        )
    if "ActualEndTime" in data:
        import aws_sdk_ssm.types.date_time

        out["actual_end_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ActualEndTime"]
        )
    if "PlannedStartTime" in data:
        import aws_sdk_ssm.types.date_time

        out["planned_start_time"] = (
            aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
                data["PlannedStartTime"]
            )
        )
    if "PlannedEndTime" in data:
        import aws_sdk_ssm.types.date_time

        out["planned_end_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["PlannedEndTime"]
        )
    return out
