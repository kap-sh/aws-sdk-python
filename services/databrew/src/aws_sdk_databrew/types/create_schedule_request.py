"""Generated from Smithy shape ``com.amazonaws.databrew#CreateScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.cron_expression
    import aws_sdk_databrew.types.job_name_list
    import aws_sdk_databrew.types.schedule_name
    import aws_sdk_databrew.types.tag_map


class CreateScheduleRequest(TypedDict, closed=True):
    job_names: NotRequired["aws_sdk_databrew.types.job_name_list.JobNameList"]
    """<p>The name or names of one or more jobs to be run.</p>"""
    cron_expression: "aws_sdk_databrew.types.cron_expression.CronExpression"
    r"""<p>The date or dates and time or times when the jobs are to be run. For more information, see <a href=\"https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html\">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this schedule.</p>"""
    name: "aws_sdk_databrew.types.schedule_name.ScheduleName"
    """<p>A unique name for the schedule. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleRequest) -> dict:
    out: dict = {}
    if "job_names" in value:
        import aws_sdk_databrew.types.job_name_list

        out["JobNames"] = aws_sdk_databrew.types.job_name_list.serialize_json(
            value["job_names"]
        )
    out["CronExpression"] = value["cron_expression"]
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateScheduleRequest:
    out: CreateScheduleRequest = {}  # type: ignore[typeddict-item]
    if "JobNames" in data:
        import aws_sdk_databrew.types.job_name_list

        out["job_names"] = aws_sdk_databrew.types.job_name_list.deserialize_json(
            data["JobNames"]
        )
    if "CronExpression" in data:
        out["cron_expression"] = data["CronExpression"]
    else:
        raise DeserializationError("CreateScheduleRequest.cron_expression required")
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateScheduleRequest.name required")
    return out
