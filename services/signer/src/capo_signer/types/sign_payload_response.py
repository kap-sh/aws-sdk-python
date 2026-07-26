"""Generated from Smithy shape ``com.amazonaws.signer#SignPayloadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.account_id
    import capo_signer.types.blob
    import capo_signer.types.job_id
    import capo_signer.types.metadata


class SignPayloadResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_signer.types.job_id.JobId"]
    """<p>Unique identifier of the signing job.</p>"""
    job_owner: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the job owner.</p>"""
    metadata: NotRequired["capo_signer.types.metadata.Metadata"]
    """<p>Information including the signing profile ARN and the signing job ID.</p>"""
    signature: NotRequired["capo_signer.types.blob.Blob"]
    """<p>A cryptographic signature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignPayloadResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "job_owner" in value:
        out["jobOwner"] = value["job_owner"]
    if "metadata" in value:
        import capo_signer.types.metadata

        out["metadata"] = capo_signer.types.metadata.serialize_json(value["metadata"])
    if "signature" in value:
        import capo_signer.types.blob

        out["signature"] = capo_signer.types.blob.serialize_json(value["signature"])
    return out


def deserialize_json(data: dict) -> SignPayloadResponse:
    out: SignPayloadResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "jobOwner" in data:
        out["job_owner"] = data["jobOwner"]
    if "metadata" in data:
        import capo_signer.types.metadata

        out["metadata"] = capo_signer.types.metadata.deserialize_json(data["metadata"])
    if "signature" in data:
        import capo_signer.types.blob

        out["signature"] = capo_signer.types.blob.deserialize_json(data["signature"])
    return out
