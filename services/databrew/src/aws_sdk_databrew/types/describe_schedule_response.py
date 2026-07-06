"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.cron_expression
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.job_name_list
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.schedule_name
    import aws_sdk_databrew.types.tag_map


class DescribeScheduleResponse(TypedDict, closed=True):
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the schedule was created.</p>"""
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The identifier (user name) of the user who created the schedule. </p>"""
    job_names: NotRequired["aws_sdk_databrew.types.job_name_list.JobNameList"]
    """<p>The name or names of one or more jobs to be run by using the schedule.</p>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The identifier (user name) of the user who last modified the schedule.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the schedule was last modified.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the schedule.</p>"""
    cron_expression: NotRequired[
        "aws_sdk_databrew.types.cron_expression.CronExpression"
    ]
    r"""<p>The date or dates and time or times when the jobs are to be run for the schedule. For more information, see <a href=\"https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html\">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags associated with this schedule.</p>"""
    name: "aws_sdk_databrew.types.schedule_name.ScheduleName"
    """<p>The name of the schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScheduleResponse) -> dict:
    out: dict = {}
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
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


def deserialize_json(data: dict) -> DescribeScheduleResponse:
    out: DescribeScheduleResponse = {}  # type: ignore[typeddict-item]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
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
        raise DeserializationError("DescribeScheduleResponse.name required")
    return out
