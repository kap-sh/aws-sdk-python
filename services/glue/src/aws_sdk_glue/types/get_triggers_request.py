"""Generated from Smithy shape ``com.amazonaws.glue#GetTriggersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.orchestration_page_size200


class GetTriggersRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if this is a continuation call.</p>"""
    dependent_job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the job to retrieve triggers for. The trigger that can start this job is returned, and if there is no such trigger, all triggers are returned.</p>"""
    max_results: NotRequired[
        "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
    ]
    """<p>The maximum size of the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTriggersRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "dependent_job_name" in value:
        out["DependentJobName"] = value["dependent_job_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTriggersRequest:
    out: GetTriggersRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DependentJobName" in data:
        out["dependent_job_name"] = data["DependentJobName"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
