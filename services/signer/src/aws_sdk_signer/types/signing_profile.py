"""Generated from Smithy shape ``com.amazonaws.signer#SigningProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.arn
    import aws_sdk_signer.types.display_name
    import aws_sdk_signer.types.platform_id
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.profile_version
    import aws_sdk_signer.types.signature_validity_period
    import aws_sdk_signer.types.signing_material
    import aws_sdk_signer.types.signing_parameters
    import aws_sdk_signer.types.signing_profile_status
    import aws_sdk_signer.types.string
    import aws_sdk_signer.types.tag_map


class SigningProfile(TypedDict, closed=True):
    profile_name: NotRequired["aws_sdk_signer.types.profile_name.ProfileName"]
    """<p>The name of the signing profile.</p>"""
    profile_version: NotRequired["aws_sdk_signer.types.profile_version.ProfileVersion"]
    """<p>The version of a signing profile.</p>"""
    profile_version_arn: NotRequired["aws_sdk_signer.types.arn.Arn"]
    """<p>The ARN of a signing profile, including the profile version.</p>"""
    signing_material: NotRequired[
        "aws_sdk_signer.types.signing_material.SigningMaterial"
    ]
    """<p>The ACM certificate that is available for use by a signing profile.</p>"""
    signature_validity_period: NotRequired[
        "aws_sdk_signer.types.signature_validity_period.SignatureValidityPeriod"
    ]
    """<p>The validity period for a signing job created using this signing profile.</p>"""
    platform_id: NotRequired["aws_sdk_signer.types.platform_id.PlatformId"]
    """<p>The ID of a platform that is available for use by a signing profile.</p>"""
    platform_display_name: NotRequired["aws_sdk_signer.types.display_name.DisplayName"]
    """<p>The name of the signing platform.</p>"""
    signing_parameters: NotRequired[
        "aws_sdk_signer.types.signing_parameters.SigningParameters"
    ]
    """<p>The parameters that are available for use by a Signer user.</p>"""
    status: NotRequired[
        "aws_sdk_signer.types.signing_profile_status.SigningProfileStatus"
    ]
    """<p>The status of a signing profile.</p>"""
    arn: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the signing profile.</p>"""
    tags: NotRequired["aws_sdk_signer.types.tag_map.TagMap"]
    """<p>A list of tags associated with the signing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfile) -> dict:
    out: dict = {}
    if "profile_name" in value:
        out["profileName"] = value["profile_name"]
    if "profile_version" in value:
        out["profileVersion"] = value["profile_version"]
    if "profile_version_arn" in value:
        out["profileVersionArn"] = value["profile_version_arn"]
    if "signing_material" in value:
        import aws_sdk_signer.types.signing_material

        out["signingMaterial"] = aws_sdk_signer.types.signing_material.serialize_json(
            value["signing_material"]
        )
    if "signature_validity_period" in value:
        import aws_sdk_signer.types.signature_validity_period

        out["signatureValidityPeriod"] = (
            aws_sdk_signer.types.signature_validity_period.serialize_json(
                value["signature_validity_period"]
            )
        )
    if "platform_id" in value:
        out["platformId"] = value["platform_id"]
    if "platform_display_name" in value:
        out["platformDisplayName"] = value["platform_display_name"]
    if "signing_parameters" in value:
        import aws_sdk_signer.types.signing_parameters

        out["signingParameters"] = (
            aws_sdk_signer.types.signing_parameters.serialize_json(
                value["signing_parameters"]
            )
        )
    if "status" in value:
        import aws_sdk_signer.types.signing_profile_status

        out["status"] = aws_sdk_signer.types.signing_profile_status.serialize_json(
            value["status"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_signer.types.tag_map

        out["tags"] = aws_sdk_signer.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SigningProfile:
    out: SigningProfile = {}  # type: ignore[typeddict-item]
    if "profileName" in data:
        out["profile_name"] = data["profileName"]
    if "profileVersion" in data:
        out["profile_version"] = data["profileVersion"]
    if "profileVersionArn" in data:
        out["profile_version_arn"] = data["profileVersionArn"]
    if "signingMaterial" in data:
        import aws_sdk_signer.types.signing_material

        out["signing_material"] = (
            aws_sdk_signer.types.signing_material.deserialize_json(
                data["signingMaterial"]
            )
        )
    if "signatureValidityPeriod" in data:
        import aws_sdk_signer.types.signature_validity_period

        out["signature_validity_period"] = (
            aws_sdk_signer.types.signature_validity_period.deserialize_json(
                data["signatureValidityPeriod"]
            )
        )
    if "platformId" in data:
        out["platform_id"] = data["platformId"]
    if "platformDisplayName" in data:
        out["platform_display_name"] = data["platformDisplayName"]
    if "signingParameters" in data:
        import aws_sdk_signer.types.signing_parameters

        out["signing_parameters"] = (
            aws_sdk_signer.types.signing_parameters.deserialize_json(
                data["signingParameters"]
            )
        )
    if "status" in data:
        import aws_sdk_signer.types.signing_profile_status

        out["status"] = aws_sdk_signer.types.signing_profile_status.deserialize_json(
            data["status"]
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_signer.types.tag_map

        out["tags"] = aws_sdk_signer.types.tag_map.deserialize_json(data["tags"])
    return out
