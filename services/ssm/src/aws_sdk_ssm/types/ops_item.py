"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.ops_item_arn
    import aws_sdk_ssm.types.ops_item_category
    import aws_sdk_ssm.types.ops_item_description
    import aws_sdk_ssm.types.ops_item_id
    import aws_sdk_ssm.types.ops_item_notifications
    import aws_sdk_ssm.types.ops_item_operational_data
    import aws_sdk_ssm.types.ops_item_priority
    import aws_sdk_ssm.types.ops_item_severity
    import aws_sdk_ssm.types.ops_item_source
    import aws_sdk_ssm.types.ops_item_status
    import aws_sdk_ssm.types.ops_item_title
    import aws_sdk_ssm.types.ops_item_type
    import aws_sdk_ssm.types.related_ops_items
    import aws_sdk_ssm.types.string


class OpsItem(TypedDict):
    created_by: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The ARN of the Amazon Web Services account that created the OpsItem.</p>"""
    ops_item_type: NotRequired["aws_sdk_ssm.types.ops_item_type.OpsItemType"]
    """<p>The type of OpsItem. Systems Manager supports the following types of OpsItems:</p> <ul> <li> <p> <code>/aws/issue</code> </p> <p>This type of OpsItem is used for default OpsItems created by OpsCenter. </p> </li> <li> <p> <code>/aws/changerequest</code> </p> <p>This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests. </p> </li> <li> <p> <code>/aws/insight</code> </p> <p>This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems. </p> </li> </ul>"""
    created_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was created.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.ops_item_description.OpsItemDescription"
    ]
    """<p>The OpsItem description.</p>"""
    last_modified_by: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The ARN of the Amazon Web Services account that last updated the OpsItem.</p>"""
    last_modified_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was last updated.</p>"""
    notifications: NotRequired[
        "aws_sdk_ssm.types.ops_item_notifications.OpsItemNotifications"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Simple Notification Service (Amazon SNS) topic where notifications are sent when this OpsItem is edited or changed.</p>"""
    priority: NotRequired["aws_sdk_ssm.types.ops_item_priority.OpsItemPriority"]
    """<p>The importance of this OpsItem in relation to other OpsItems in the system.</p>"""
    related_ops_items: NotRequired[
        "aws_sdk_ssm.types.related_ops_items.RelatedOpsItems"
    ]
    """<p>One or more OpsItems that share something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.</p>"""
    status: NotRequired["aws_sdk_ssm.types.ops_item_status.OpsItemStatus"]
    """<p>The OpsItem status. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html\">Editing OpsItem details</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    ops_item_id: NotRequired["aws_sdk_ssm.types.ops_item_id.OpsItemId"]
    """<p>The ID of the OpsItem.</p>"""
    version: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The version of this OpsItem. Each time the OpsItem is edited the version number increments by one.</p>"""
    title: NotRequired["aws_sdk_ssm.types.ops_item_title.OpsItemTitle"]
    """<p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>"""
    source: NotRequired["aws_sdk_ssm.types.ops_item_source.OpsItemSource"]
    """<p>The origin of the OpsItem, such as Amazon EC2 or Systems Manager. The impacted resource is a subset of source.</p>"""
    operational_data: NotRequired[
        "aws_sdk_ssm.types.ops_item_operational_data.OpsItemOperationalData"
    ]
    """<p>Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.</p> <important> <p>Operational data keys <i>can't</i> begin with the following: <code>amazon</code>, <code>aws</code>, <code>amzn</code>, <code>ssm</code>, <code>/amazon</code>, <code>/aws</code>, <code>/amzn</code>, <code>/ssm</code>.</p> </important> <p>You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the <a>DescribeOpsItems</a> API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the <a>GetOpsItem</a> API operation).</p> <p>Use the <code>/aws/resources</code> key in OperationalData to specify a related resource in the request. Use the <code>/aws/automations</code> key in OperationalData to associate an Automation runbook with the OpsItem. To view Amazon Web Services CLI example commands that use these keys, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html\">Creating OpsItems manually</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    category: NotRequired["aws_sdk_ssm.types.ops_item_category.OpsItemCategory"]
    """<p>An OpsItem category. Category options include: Availability, Cost, Performance, Recovery, Security.</p>"""
    severity: NotRequired["aws_sdk_ssm.types.ops_item_severity.OpsItemSeverity"]
    """<p>The severity of the OpsItem. Severity options range from 1 to 4.</p>"""
    actual_start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow started. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    actual_end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow ended. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    ops_item_arn: NotRequired["aws_sdk_ssm.types.ops_item_arn.OpsItemArn"]
    """<p>The OpsItem Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItem) -> dict:
    out: dict = {}
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "ops_item_type" in value:
        out["OpsItemType"] = value["ops_item_type"]
    if "created_time" in value:
        import aws_sdk_ssm.types.date_time

        out["CreatedTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_time" in value:
        import aws_sdk_ssm.types.date_time

        out["LastModifiedTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "notifications" in value:
        import aws_sdk_ssm.types.ops_item_notifications

        out["Notifications"] = (
            aws_sdk_ssm.types.ops_item_notifications.serialize_aws_json_1_1(
                value["notifications"]
            )
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "related_ops_items" in value:
        import aws_sdk_ssm.types.related_ops_items

        out["RelatedOpsItems"] = (
            aws_sdk_ssm.types.related_ops_items.serialize_aws_json_1_1(
                value["related_ops_items"]
            )
        )
    if "status" in value:
        import aws_sdk_ssm.types.ops_item_status

        out["Status"] = aws_sdk_ssm.types.ops_item_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "version" in value:
        out["Version"] = value["version"]
    if "title" in value:
        out["Title"] = value["title"]
    if "source" in value:
        out["Source"] = value["source"]
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
    if "ops_item_arn" in value:
        out["OpsItemArn"] = value["ops_item_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItem:
    out: OpsItem = {}  # type: ignore[typeddict-item]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "OpsItemType" in data:
        out["ops_item_type"] = data["OpsItemType"]
    if "CreatedTime" in data:
        import aws_sdk_ssm.types.date_time

        out["created_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedTime" in data:
        import aws_sdk_ssm.types.date_time

        out["last_modified_time"] = (
            aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "Notifications" in data:
        import aws_sdk_ssm.types.ops_item_notifications

        out["notifications"] = (
            aws_sdk_ssm.types.ops_item_notifications.deserialize_aws_json_1_1(
                data["Notifications"]
            )
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "RelatedOpsItems" in data:
        import aws_sdk_ssm.types.related_ops_items

        out["related_ops_items"] = (
            aws_sdk_ssm.types.related_ops_items.deserialize_aws_json_1_1(
                data["RelatedOpsItems"]
            )
        )
    if "Status" in data:
        import aws_sdk_ssm.types.ops_item_status

        out["status"] = aws_sdk_ssm.types.ops_item_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Source" in data:
        out["source"] = data["Source"]
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
    if "OpsItemArn" in data:
        out["ops_item_arn"] = data["OpsItemArn"]
    return out
