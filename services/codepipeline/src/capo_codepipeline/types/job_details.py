"""Generated from Smithy shape ``com.amazonaws.codepipeline#JobDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.account_id
    import capo_codepipeline.types.job_data
    import capo_codepipeline.types.job_id


class JobDetails(TypedDict, closed=True):
    id: NotRequired["capo_codepipeline.types.job_id.JobId"]
    """<p>The unique system-generated ID of the job.</p>"""
    data: NotRequired["capo_codepipeline.types.job_data.JobData"]
    """<p>Represents other information about a job required for a job worker to complete the job. </p>"""
    account_id: NotRequired["capo_codepipeline.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID associated with the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "data" in value:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.serialize_aws_json_1_1(
            value["data"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobDetails:
    out: JobDetails = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "data" in data:
        import capo_codepipeline.types.job_data

        out["data"] = capo_codepipeline.types.job_data.deserialize_aws_json_1_1(
            data["data"]
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out
