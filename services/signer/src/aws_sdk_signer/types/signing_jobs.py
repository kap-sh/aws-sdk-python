"""Generated from Smithy shape ``com.amazonaws.signer#SigningJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_signer.types.signing_job

SigningJobs: TypeAlias = list["aws_sdk_signer.types.signing_job.SigningJob"]


# --- restJson1 ser/de ---
def serialize_json(value: SigningJobs) -> list:
    import aws_sdk_signer.types.signing_job

    out: list = []
    for item in value:
        out.append(aws_sdk_signer.types.signing_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> SigningJobs:
    import aws_sdk_signer.types.signing_job

    out: SigningJobs = []
    for item in data:
        out.append(aws_sdk_signer.types.signing_job.deserialize_json(item))
    return out
