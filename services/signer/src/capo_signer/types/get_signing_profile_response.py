"""Generated from Smithy shape ``com.amazonaws.signer#GetSigningProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.arn
    import capo_signer.types.display_name
    import capo_signer.types.platform_id
    import capo_signer.types.profile_name
    import capo_signer.types.profile_version
    import capo_signer.types.signature_validity_period
    import capo_signer.types.signing_material
    import capo_signer.types.signing_parameters
    import capo_signer.types.signing_platform_overrides
    import capo_signer.types.signing_profile_revocation_record
    import capo_signer.types.signing_profile_status
    import capo_signer.types.string
    import capo_signer.types.tag_map


class GetSigningProfileResponse(TypedDict, closed=True):
    profile_name: NotRequired["capo_signer.types.profile_name.ProfileName"]
    """<p>The name of the target signing profile.</p>"""
    profile_version: NotRequired["capo_signer.types.profile_version.ProfileVersion"]
    """<p>The current version of the signing profile.</p>"""
    profile_version_arn: NotRequired["capo_signer.types.arn.Arn"]
    """<p>The signing profile ARN, including the profile version.</p>"""
    revocation_record: NotRequired[
        "capo_signer.types.signing_profile_revocation_record.SigningProfileRevocationRecord"
    ]
    signing_material: NotRequired["capo_signer.types.signing_material.SigningMaterial"]
    """<p>The ARN of the certificate that the target profile uses for signing operations.</p>"""
    platform_id: NotRequired["capo_signer.types.platform_id.PlatformId"]
    """<p>The ID of the platform that is used by the target signing profile.</p>"""
    platform_display_name: NotRequired["capo_signer.types.display_name.DisplayName"]
    """<p>A human-readable name for the signing platform associated with the signing profile.</p>"""
    signature_validity_period: NotRequired[
        "capo_signer.types.signature_validity_period.SignatureValidityPeriod"
    ]
    overrides: NotRequired[
        "capo_signer.types.signing_platform_overrides.SigningPlatformOverrides"
    ]
    """<p>A list of overrides applied by the target signing profile for signing operations.</p>"""
    signing_parameters: NotRequired[
        "capo_signer.types.signing_parameters.SigningParameters"
    ]
    """<p>A map of key-value pairs for signing operations that is attached to the target signing profile.</p>"""
    status: NotRequired["capo_signer.types.signing_profile_status.SigningProfileStatus"]
    """<p>The status of the target signing profile.</p>"""
    status_reason: NotRequired["capo_signer.types.string.String"]
    """<p>Reason for the status of the target signing profile.</p>"""
    arn: NotRequired["capo_signer.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the signing profile.</p>"""
    tags: NotRequired["capo_signer.types.tag_map.TagMap"]
    """<p>A list of tags associated with the signing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSigningProfileResponse) -> dict:
    out: dict = {}
    if "profile_name" in value:
        out["profileName"] = value["profile_name"]
    if "profile_version" in value:
        out["profileVersion"] = value["profile_version"]
    if "profile_version_arn" in value:
        out["profileVersionArn"] = value["profile_version_arn"]
    if "revocation_record" in value:
        import capo_signer.types.signing_profile_revocation_record

        out["revocationRecord"] = (
            capo_signer.types.signing_profile_revocation_record.serialize_json(
                value["revocation_record"]
            )
        )
    if "signing_material" in value:
        import capo_signer.types.signing_material

        out["signingMaterial"] = capo_signer.types.signing_material.serialize_json(
            value["signing_material"]
        )
    if "platform_id" in value:
        out["platformId"] = value["platform_id"]
    if "platform_display_name" in value:
        out["platformDisplayName"] = value["platform_display_name"]
    if "signature_validity_period" in value:
        import capo_signer.types.signature_validity_period

        out["signatureValidityPeriod"] = (
            capo_signer.types.signature_validity_period.serialize_json(
                value["signature_validity_period"]
            )
        )
    if "overrides" in value:
        import capo_signer.types.signing_platform_overrides

        out["overrides"] = capo_signer.types.signing_platform_overrides.serialize_json(
            value["overrides"]
        )
    if "signing_parameters" in value:
        import capo_signer.types.signing_parameters

        out["signingParameters"] = capo_signer.types.signing_parameters.serialize_json(
            value["signing_parameters"]
        )
    if "status" in value:
        import capo_signer.types.signing_profile_status

        out["status"] = capo_signer.types.signing_profile_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_signer.types.tag_map

        out["tags"] = capo_signer.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSigningProfileResponse:
    out: GetSigningProfileResponse = {}  # type: ignore[typeddict-item]
    if "profileName" in data:
        out["profile_name"] = data["profileName"]
    if "profileVersion" in data:
        out["profile_version"] = data["profileVersion"]
    if "profileVersionArn" in data:
        out["profile_version_arn"] = data["profileVersionArn"]
    if "revocationRecord" in data:
        import capo_signer.types.signing_profile_revocation_record

        out["revocation_record"] = (
            capo_signer.types.signing_profile_revocation_record.deserialize_json(
                data["revocationRecord"]
            )
        )
    if "signingMaterial" in data:
        import capo_signer.types.signing_material

        out["signing_material"] = capo_signer.types.signing_material.deserialize_json(
            data["signingMaterial"]
        )
    if "platformId" in data:
        out["platform_id"] = data["platformId"]
    if "platformDisplayName" in data:
        out["platform_display_name"] = data["platformDisplayName"]
    if "signatureValidityPeriod" in data:
        import capo_signer.types.signature_validity_period

        out["signature_validity_period"] = (
            capo_signer.types.signature_validity_period.deserialize_json(
                data["signatureValidityPeriod"]
            )
        )
    if "overrides" in data:
        import capo_signer.types.signing_platform_overrides

        out["overrides"] = (
            capo_signer.types.signing_platform_overrides.deserialize_json(
                data["overrides"]
            )
        )
    if "signingParameters" in data:
        import capo_signer.types.signing_parameters

        out["signing_parameters"] = (
            capo_signer.types.signing_parameters.deserialize_json(
                data["signingParameters"]
            )
        )
    if "status" in data:
        import capo_signer.types.signing_profile_status

        out["status"] = capo_signer.types.signing_profile_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import capo_signer.types.tag_map

        out["tags"] = capo_signer.types.tag_map.deserialize_json(data["tags"])
    return out
