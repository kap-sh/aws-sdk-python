"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.job_parameters
    import aws_sdk_glacier.types.string


class InitiateJobInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    job_parameters: NotRequired["aws_sdk_glacier.types.job_parameters.JobParameters"]
    """<p>Provides options for specifying job information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateJobInput) -> dict:
    out: dict = {}
    if "job_parameters" in value:
        import aws_sdk_glacier.types.job_parameters

        out["jobParameters"] = aws_sdk_glacier.types.job_parameters.serialize_json(
            value["job_parameters"]
        )
    return out


def deserialize_json(data: dict) -> InitiateJobInput:
    out: InitiateJobInput = {}  # type: ignore[typeddict-item]
    if "jobParameters" in data:
        import aws_sdk_glacier.types.job_parameters

        out["job_parameters"] = aws_sdk_glacier.types.job_parameters.deserialize_json(
            data["jobParameters"]
        )
    return out
