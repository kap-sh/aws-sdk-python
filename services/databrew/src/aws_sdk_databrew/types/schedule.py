"""Generated from Smithy shape ``com.amazonaws.databrew#Schedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.account_id
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.cron_expression
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.job_name_list
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.schedule_name
    import aws_sdk_databrew.types.tag_map


class Schedule(TypedDict):
    account_id: NotRequired["aws_sdk_databrew.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the schedule.</p>"""
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the schedule.</p>"""
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the schedule was created.</p>"""
    job_names: NotRequired["aws_sdk_databrew.types.job_name_list.JobNameList"]
    """<p>A list of jobs to be run, according to the schedule.</p>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the schedule.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time when the schedule was last modified.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the schedule.</p>"""
    cron_expression: NotRequired[
        "aws_sdk_databrew.types.cron_expression.CronExpression"
    ]
    """<p>The dates and times when the job is to run. For more information, see <a href=\"https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html\">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the schedule.</p>"""
    name: "aws_sdk_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Schedule) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "job_names" in value:
        import aws_sdk_databrew.types.job_name_list

        out["JobNames"] = aws_sdk_databrew.types.job_name_list.serialize_json(
            value["job_names"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "cron_expression" in value:
        out["CronExpression"] = value["cron_expression"]
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Schedule:
    out: Schedule = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "JobNames" in data:
        import aws_sdk_databrew.types.job_name_list

        out["job_names"] = aws_sdk_databrew.types.job_name_list.deserialize_json(
            data["JobNames"]
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "CronExpression" in data:
        out["cron_expression"] = data["CronExpression"]
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Schedule.name required")
    return out
