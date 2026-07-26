"""Generated from Smithy shape ``com.amazonaws.signerdata#GetRevocationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_signer_data.types.arn
    import capo_signer_data.types.certificate_hashes
    import capo_signer_data.types.platform_id


class GetRevocationStatusRequest(TypedDict, closed=True):
    signature_timestamp: "datetime.datetime"
    """<p>The timestamp when the artifact was signed, in ISO 8601 format.</p>"""
    platform_id: "capo_signer_data.types.platform_id.PlatformId"
    """<p>The platform identifier for the signing platform used.</p>"""
    profile_version_arn: "capo_signer_data.types.arn.Arn"
    """<p>The ARN of the signing profile version used to sign the artifact.</p>"""
    job_arn: "capo_signer_data.types.arn.Arn"
    """<p>The ARN of the signing job that produced the signature.</p>"""
    certificate_hashes: "capo_signer_data.types.certificate_hashes.CertificateHashes"
    """<p>List of certificate hashes to check for revocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRevocationStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRevocationStatusRequest:
    out: GetRevocationStatusRequest = {}  # type: ignore[typeddict-item]
    return out
