"""Generated from Smithy shape ``com.amazonaws.signer#SigningJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.account_id
    import aws_sdk_signer.types.bool
    import aws_sdk_signer.types.display_name
    import aws_sdk_signer.types.job_id
    import aws_sdk_signer.types.platform_id
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.profile_version
    import aws_sdk_signer.types.signed_object
    import aws_sdk_signer.types.signing_material
    import aws_sdk_signer.types.signing_status
    import aws_sdk_signer.types.source
    import aws_sdk_signer.types.timestamp


class SigningJob(TypedDict):
    job_id: NotRequired["aws_sdk_signer.types.job_id.JobId"]
    """<p>The ID of the signing job.</p>"""
    source: NotRequired["aws_sdk_signer.types.source.Source"]
    """<p>A <code>Source</code> that contains information about a signing job's code image source.</p>"""
    signed_object: NotRequired["aws_sdk_signer.types.signed_object.SignedObject"]
    """<p>A <code>SignedObject</code> structure that contains information about a signing job's signed code image.</p>"""
    signing_material: NotRequired[
        "aws_sdk_signer.types.signing_material.SigningMaterial"
    ]
    """<p>A <code>SigningMaterial</code> object that contains the Amazon Resource Name (ARN) of the certificate used for the signing job.</p>"""
    created_at: NotRequired["aws_sdk_signer.types.timestamp.Timestamp"]
    """<p>The date and time that the signing job was created.</p>"""
    status: NotRequired["aws_sdk_signer.types.signing_status.SigningStatus"]
    """<p>The status of the signing job.</p>"""
    is_revoked: "aws_sdk_signer.types.bool.bool"
    """<p>Indicates whether the signing job is revoked.</p>"""
    profile_name: NotRequired["aws_sdk_signer.types.profile_name.ProfileName"]
    """<p>The name of the signing profile that created a signing job.</p>"""
    profile_version: NotRequired["aws_sdk_signer.types.profile_version.ProfileVersion"]
    """<p>The version of the signing profile that created a signing job.</p>"""
    platform_id: NotRequired["aws_sdk_signer.types.platform_id.PlatformId"]
    """<p>The unique identifier for a signing platform.</p>"""
    platform_display_name: NotRequired["aws_sdk_signer.types.display_name.DisplayName"]
    """<p>The name of a signing platform.</p>"""
    signature_expires_at: NotRequired["aws_sdk_signer.types.timestamp.Timestamp"]
    """<p>The time when the signature of a signing job expires.</p>"""
    job_owner: NotRequired["aws_sdk_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the job owner.</p>"""
    job_invoker: NotRequired["aws_sdk_signer.types.account_id.AccountId"]
    """<p>The AWS account ID of the job invoker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "source" in value:
        import aws_sdk_signer.types.source

        out["source"] = aws_sdk_signer.types.source.serialize_json(value["source"])
    if "signed_object" in value:
        import aws_sdk_signer.types.signed_object

        out["signedObject"] = aws_sdk_signer.types.signed_object.serialize_json(
            value["signed_object"]
        )
    if "signing_material" in value:
        import aws_sdk_signer.types.signing_material

        out["signingMaterial"] = aws_sdk_signer.types.signing_material.serialize_json(
            value["signing_material"]
        )
    if "created_at" in value:
        import aws_sdk_signer.types.timestamp

        out["createdAt"] = aws_sdk_signer.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "status" in value:
        import aws_sdk_signer.types.signing_status

        out["status"] = aws_sdk_signer.types.signing_status.serialize_json(
            value["status"]
        )
    out["isRevoked"] = value.get("is_revoked", False)
    if "profile_name" in value:
        out["profileName"] = value["profile_name"]
    if "profile_version" in value:
        out["profileVersion"] = value["profile_version"]
    if "platform_id" in value:
        out["platformId"] = value["platform_id"]
    if "platform_display_name" in value:
        out["platformDisplayName"] = value["platform_display_name"]
    if "signature_expires_at" in value:
        import aws_sdk_signer.types.timestamp

        out["signatureExpiresAt"] = aws_sdk_signer.types.timestamp.serialize_json(
            value["signature_expires_at"]
        )
    if "job_owner" in value:
        out["jobOwner"] = value["job_owner"]
    if "job_invoker" in value:
        out["jobInvoker"] = value["job_invoker"]
    return out


def deserialize_json(data: dict) -> SigningJob:
    out: SigningJob = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "source" in data:
        import aws_sdk_signer.types.source

        out["source"] = aws_sdk_signer.types.source.deserialize_json(data["source"])
    if "signedObject" in data:
        import aws_sdk_signer.types.signed_object

        out["signed_object"] = aws_sdk_signer.types.signed_object.deserialize_json(
            data["signedObject"]
        )
    if "signingMaterial" in data:
        import aws_sdk_signer.types.signing_material

        out["signing_material"] = (
            aws_sdk_signer.types.signing_material.deserialize_json(
                data["signingMaterial"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_signer.types.timestamp

        out["created_at"] = aws_sdk_signer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "status" in data:
        import aws_sdk_signer.types.signing_status

        out["status"] = aws_sdk_signer.types.signing_status.deserialize_json(
            data["status"]
        )
    if "isRevoked" in data:
        out["is_revoked"] = data["isRevoked"]
    else:
        out["is_revoked"] = False
    if "profileName" in data:
        out["profile_name"] = data["profileName"]
    if "profileVersion" in data:
        out["profile_version"] = data["profileVersion"]
    if "platformId" in data:
        out["platform_id"] = data["platformId"]
    if "platformDisplayName" in data:
        out["platform_display_name"] = data["platformDisplayName"]
    if "signatureExpiresAt" in data:
        import aws_sdk_signer.types.timestamp

        out["signature_expires_at"] = aws_sdk_signer.types.timestamp.deserialize_json(
            data["signatureExpiresAt"]
        )
    if "jobOwner" in data:
        out["job_owner"] = data["jobOwner"]
    if "jobInvoker" in data:
        out["job_invoker"] = data["jobInvoker"]
    return out
