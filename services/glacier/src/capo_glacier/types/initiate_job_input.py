"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.job_parameters
    import capo_glacier.types.string


class InitiateJobInput(TypedDict, closed=True):
    account_id: "capo_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "capo_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    job_parameters: NotRequired["capo_glacier.types.job_parameters.JobParameters"]
    """<p>Provides options for specifying job information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateJobInput) -> dict:
    out: dict = {}
    if "job_parameters" in value:
        import capo_glacier.types.job_parameters

        out["jobParameters"] = capo_glacier.types.job_parameters.serialize_json(
            value["job_parameters"]
        )
    return out


def deserialize_json(data: dict) -> InitiateJobInput:
    out: InitiateJobInput = {}  # type: ignore[typeddict-item]
    if "jobParameters" in data:
        import capo_glacier.types.job_parameters

        out["job_parameters"] = capo_glacier.types.job_parameters.deserialize_json(
            data["jobParameters"]
        )
    return out
