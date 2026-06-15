"""Generated from Smithy shape ``com.amazonaws.signer#GetRevocationStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.arn
    import aws_sdk_signer.types.certificate_hashes
    import aws_sdk_signer.types.platform_id
    import aws_sdk_signer.types.timestamp


class GetRevocationStatusRequest(TypedDict):
    signature_timestamp: "aws_sdk_signer.types.timestamp.Timestamp"
    """<p>The timestamp of the signature that validates the profile or job.</p>"""
    platform_id: "aws_sdk_signer.types.platform_id.PlatformId"
    """<p>The ID of a signing platform. </p>"""
    profile_version_arn: "aws_sdk_signer.types.arn.Arn"
    """<p>The version of a signing profile.</p>"""
    job_arn: "aws_sdk_signer.types.arn.Arn"
    """<p>The ARN of a signing job.</p>"""
    certificate_hashes: "aws_sdk_signer.types.certificate_hashes.CertificateHashes"
    r"""<p>A list of composite signed hashes that identify certificates.</p> <p>A certificate identifier consists of a subject certificate TBS hash (signed by the parent CA) combined with a parent CA TBS hash (signed by the parent CA’s CA). Root certificates are defined as their own CA.</p> <p>The following example shows how to calculate a hash for this parameter using OpenSSL commands: </p> <p> <code>openssl asn1parse -in childCert.pem -strparse 4 -out childCert.tbs</code> </p> <p> <code>openssl sha384 < childCert.tbs -binary > childCertTbsHash</code> </p> <p> <code>openssl asn1parse -in parentCert.pem -strparse 4 -out parentCert.tbs</code> </p> <p> <code>openssl sha384 < parentCert.tbs -binary > parentCertTbsHash xxd -p childCertTbsHash > certificateHash.hex xxd -p parentCertTbsHash >> certificateHash.hex</code> </p> <p> <code>cat certificateHash.hex | tr -d '\n'</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRevocationStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRevocationStatusRequest:
    out: GetRevocationStatusRequest = {}  # type: ignore[typeddict-item]
    return out
