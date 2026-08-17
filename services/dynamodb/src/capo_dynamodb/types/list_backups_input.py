"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListBackupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_arn
    import capo_dynamodb.types.backup_type_filter
    import capo_dynamodb.types.backups_input_limit
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.time_range_lower_bound
    import capo_dynamodb.types.time_range_upper_bound


class ListBackupsInput(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>Lists the backups from the table specified in <code>TableName</code>. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    limit: NotRequired["capo_dynamodb.types.backups_input_limit.BackupsInputLimit"]
    """<p>Maximum number of backups to return at once.</p>"""
    time_range_lower_bound: NotRequired[
        "capo_dynamodb.types.time_range_lower_bound.TimeRangeLowerBound"
    ]
    """<p>Only backups created after this time are listed. <code>TimeRangeLowerBound</code> is inclusive.</p>"""
    time_range_upper_bound: NotRequired[
        "capo_dynamodb.types.time_range_upper_bound.TimeRangeUpperBound"
    ]
    """<p>Only backups created before this time are listed. <code>TimeRangeUpperBound</code> is exclusive. </p>"""
    exclusive_start_backup_arn: NotRequired["capo_dynamodb.types.backup_arn.BackupArn"]
    """<p> <code>LastEvaluatedBackupArn</code> is the Amazon Resource Name (ARN) of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the <code>ExclusiveStartBackupArn</code> of a new <code>ListBackups</code> operation in order to fetch the next page of results. </p>"""
    backup_type: NotRequired["capo_dynamodb.types.backup_type_filter.BackupTypeFilter"]
    """<p>The backups from the table specified by <code>BackupType</code> are listed.</p> <p>Where <code>BackupType</code> can be:</p> <ul> <li> <p> <code>USER</code> - On-demand backup created by you. (The default setting if no other backup types are specified.)</p> </li> <li> <p> <code>SYSTEM</code> - On-demand backup automatically created by DynamoDB.</p> </li> <li> <p> <code>ALL</code> - All types of on-demand backups (USER and SYSTEM).</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBackupsInput) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "time_range_lower_bound" in value:
        import capo_dynamodb.types.time_range_lower_bound

        out["TimeRangeLowerBound"] = (
            capo_dynamodb.types.time_range_lower_bound.serialize_aws_json_1_0(
                value["time_range_lower_bound"]
            )
        )
    if "time_range_upper_bound" in value:
        import capo_dynamodb.types.time_range_upper_bound

        out["TimeRangeUpperBound"] = (
            capo_dynamodb.types.time_range_upper_bound.serialize_aws_json_1_0(
                value["time_range_upper_bound"]
            )
        )
    if "exclusive_start_backup_arn" in value:
        out["ExclusiveStartBackupArn"] = value["exclusive_start_backup_arn"]
    if "backup_type" in value:
        import capo_dynamodb.types.backup_type_filter

        out["BackupType"] = (
            capo_dynamodb.types.backup_type_filter.serialize_aws_json_1_0(
                value["backup_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBackupsInput:
    out: ListBackupsInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("TimeRangeLowerBound") is not None:
        import capo_dynamodb.types.time_range_lower_bound

        out["time_range_lower_bound"] = (
            capo_dynamodb.types.time_range_lower_bound.deserialize_aws_json_1_0(
                data["TimeRangeLowerBound"]
            )
        )
    if data.get("TimeRangeUpperBound") is not None:
        import capo_dynamodb.types.time_range_upper_bound

        out["time_range_upper_bound"] = (
            capo_dynamodb.types.time_range_upper_bound.deserialize_aws_json_1_0(
                data["TimeRangeUpperBound"]
            )
        )
    if data.get("ExclusiveStartBackupArn") is not None:
        out["exclusive_start_backup_arn"] = data["ExclusiveStartBackupArn"]
    if data.get("BackupType") is not None:
        import capo_dynamodb.types.backup_type_filter

        out["backup_type"] = (
            capo_dynamodb.types.backup_type_filter.deserialize_aws_json_1_0(
                data["BackupType"]
            )
        )
    return out
