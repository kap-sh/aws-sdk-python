"""Generated from Smithy shape ``com.amazonaws.glue#RunIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class RunIdentifier(TypedDict, closed=True):
    run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Run ID.</p>"""
    job_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Job Run ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunIdentifier) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RunIdentifier:
    out: RunIdentifier = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    return out
