"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_source
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.timestamp


class DataQualityResultDescription(TypedDict, closed=True):
    result_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique result ID for this data quality result.</p>"""
    data_source: NotRequired["capo_glue.types.data_source.DataSource"]
    """<p>The table name associated with the data quality result.</p>"""
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The job name associated with the data quality result.</p>"""
    job_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The job run ID associated with the data quality result.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time that the run started for this data quality result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultDescription) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
    if "data_source" in value:
        import capo_glue.types.data_source

        out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "started_on" in value:
        import capo_glue.types.timestamp

        out["StartedOn"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityResultDescription:
    out: DataQualityResultDescription = {}  # type: ignore[typeddict-item]
    if "ResultId" in data:
        out["result_id"] = data["ResultId"]
    if "DataSource" in data:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    if "StartedOn" in data:
        import capo_glue.types.timestamp

        out["started_on"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    return out
