"""Generated from Smithy shape ``com.amazonaws.signer#PutSigningProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_signer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signer.types.platform_id
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.signature_validity_period
    import aws_sdk_signer.types.signing_material
    import aws_sdk_signer.types.signing_parameters
    import aws_sdk_signer.types.signing_platform_overrides
    import aws_sdk_signer.types.tag_map


class PutSigningProfileRequest(TypedDict, closed=True):
    profile_name: "aws_sdk_signer.types.profile_name.ProfileName"
    """<p>The name of the signing profile to be created.</p>"""
    signing_material: NotRequired[
        "aws_sdk_signer.types.signing_material.SigningMaterial"
    ]
    """<p>The AWS Certificate Manager certificate that will be used to sign code with the new signing profile.</p>"""
    signature_validity_period: NotRequired[
        "aws_sdk_signer.types.signature_validity_period.SignatureValidityPeriod"
    ]
    """<p>The default validity period override for any signature generated using this signing profile. If unspecified, the default is 135 months.</p>"""
    platform_id: "aws_sdk_signer.types.platform_id.PlatformId"
    """<p>The ID of the signing platform to be created.</p>"""
    overrides: NotRequired[
        "aws_sdk_signer.types.signing_platform_overrides.SigningPlatformOverrides"
    ]
    """<p>A subfield of <code>platform</code>. This specifies any different configuration options that you want to apply to the chosen platform (such as a different <code>hash-algorithm</code> or <code>signing-algorithm</code>).</p>"""
    signing_parameters: NotRequired[
        "aws_sdk_signer.types.signing_parameters.SigningParameters"
    ]
    """<p>Map of key-value pairs for signing. These can include any information that you want to use during signing.</p>"""
    tags: NotRequired["aws_sdk_signer.types.tag_map.TagMap"]
    """<p>Tags to be associated with the signing profile that is being created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSigningProfileRequest) -> dict:
    out: dict = {}
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
    out["platformId"] = value["platform_id"]
    if "overrides" in value:
        import aws_sdk_signer.types.signing_platform_overrides

        out["overrides"] = (
            aws_sdk_signer.types.signing_platform_overrides.serialize_json(
                value["overrides"]
            )
        )
    if "signing_parameters" in value:
        import aws_sdk_signer.types.signing_parameters

        out["signingParameters"] = (
            aws_sdk_signer.types.signing_parameters.serialize_json(
                value["signing_parameters"]
            )
        )
    if "tags" in value:
        import aws_sdk_signer.types.tag_map

        out["tags"] = aws_sdk_signer.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PutSigningProfileRequest:
    out: PutSigningProfileRequest = {}  # type: ignore[typeddict-item]
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
    else:
        raise DeserializationError("PutSigningProfileRequest.platform_id required")
    if "overrides" in data:
        import aws_sdk_signer.types.signing_platform_overrides

        out["overrides"] = (
            aws_sdk_signer.types.signing_platform_overrides.deserialize_json(
                data["overrides"]
            )
        )
    if "signingParameters" in data:
        import aws_sdk_signer.types.signing_parameters

        out["signing_parameters"] = (
            aws_sdk_signer.types.signing_parameters.deserialize_json(
                data["signingParameters"]
            )
        )
    if "tags" in data:
        import aws_sdk_signer.types.tag_map

        out["tags"] = aws_sdk_signer.types.tag_map.deserialize_json(data["tags"])
    return out
