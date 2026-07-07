"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp


class DataQualityResultDescription(TypedDict, closed=True):
    result_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique result ID for this data quality result.</p>"""
    data_source: NotRequired["aws_sdk_glue.types.data_source.DataSource"]
    """<p>The table name associated with the data quality result.</p>"""
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The job name associated with the data quality result.</p>"""
    job_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The job run ID associated with the data quality result.</p>"""
    started_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that the run started for this data quality result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultDescription) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
    if "data_source" in value:
        import aws_sdk_glue.types.data_source

        out["DataSource"] = aws_sdk_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "started_on" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityResultDescription:
    out: DataQualityResultDescription = {}  # type: ignore[typeddict-item]
    if "ResultId" in data:
        out["result_id"] = data["ResultId"]
    if "DataSource" in data:
        import aws_sdk_glue.types.data_source

        out["data_source"] = aws_sdk_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    if "StartedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["started_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    return out
