"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultFilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_source
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp


class DataQualityResultFilterCriteria(TypedDict):
    data_source: NotRequired["aws_sdk_glue.types.data_source.DataSource"]
    """<p>Filter results by the specified data source. For example, retrieving all results for an Glue table.</p>"""
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Filter results by the specified job name.</p>"""
    job_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>Filter results by the specified job run ID.</p>"""
    started_after: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>Filter results by runs that started after this time.</p>"""
    started_before: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>Filter results by runs that started before this time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultFilterCriteria) -> dict:
    out: dict = {}
    if "data_source" in value:
        import aws_sdk_glue.types.data_source

        out["DataSource"] = aws_sdk_glue.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "started_after" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedAfter"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_after"]
        )
    if "started_before" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedBefore"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_before"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityResultFilterCriteria:
    out: DataQualityResultFilterCriteria = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import aws_sdk_glue.types.data_source

        out["data_source"] = aws_sdk_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    if "StartedAfter" in data:
        import aws_sdk_glue.types.timestamp

        out["started_after"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedAfter"]
        )
    if "StartedBefore" in data:
        import aws_sdk_glue.types.timestamp

        out["started_before"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedBefore"]
        )
    return out
