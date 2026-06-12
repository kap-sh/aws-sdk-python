"""Generated from Smithy shape ``com.amazonaws.signer#SigningPlatform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.bool
    import aws_sdk_signer.types.category
    import aws_sdk_signer.types.max_size_in_mb
    import aws_sdk_signer.types.signing_configuration
    import aws_sdk_signer.types.signing_image_format
    import aws_sdk_signer.types.string


class SigningPlatform(TypedDict):
    platform_id: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The ID of a signing platform.</p>"""
    display_name: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The display name of a signing platform.</p>"""
    partner: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>Any partner entities linked to a signing platform.</p>"""
    target: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The types of targets that can be signed by a signing platform.</p>"""
    category: NotRequired["aws_sdk_signer.types.category.Category"]
    """<p>The category of a signing platform.</p>"""
    signing_configuration: NotRequired[
        "aws_sdk_signer.types.signing_configuration.SigningConfiguration"
    ]
    """<p>The configuration of a signing platform. This includes the designated hash algorithm and encryption algorithm of a signing platform.</p>"""
    signing_image_format: NotRequired[
        "aws_sdk_signer.types.signing_image_format.SigningImageFormat"
    ]
    max_size_in_mb: "aws_sdk_signer.types.max_size_in_mb.MaxSizeInMB"
    """<p>The maximum size (in MB) of code that can be signed by a signing platform.</p>"""
    revocation_supported: "aws_sdk_signer.types.bool.bool"
    """<p>Indicates whether revocation is supported for the platform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningPlatform) -> dict:
    out: dict = {}
    if "platform_id" in value:
        out["platformId"] = value["platform_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "partner" in value:
        out["partner"] = value["partner"]
    if "target" in value:
        out["target"] = value["target"]
    if "category" in value:
        import aws_sdk_signer.types.category

        out["category"] = aws_sdk_signer.types.category.serialize_json(
            value["category"]
        )
    if "signing_configuration" in value:
        import aws_sdk_signer.types.signing_configuration

        out["signingConfiguration"] = (
            aws_sdk_signer.types.signing_configuration.serialize_json(
                value["signing_configuration"]
            )
        )
    if "signing_image_format" in value:
        import aws_sdk_signer.types.signing_image_format

        out["signingImageFormat"] = (
            aws_sdk_signer.types.signing_image_format.serialize_json(
                value["signing_image_format"]
            )
        )
    out["maxSizeInMB"] = value.get("max_size_in_mb", 0)
    out["revocationSupported"] = value.get("revocation_supported", False)
    return out


def deserialize_json(data: dict) -> SigningPlatform:
    out: SigningPlatform = {}  # type: ignore[typeddict-item]
    if "platformId" in data:
        out["platform_id"] = data["platformId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "partner" in data:
        out["partner"] = data["partner"]
    if "target" in data:
        out["target"] = data["target"]
    if "category" in data:
        import aws_sdk_signer.types.category

        out["category"] = aws_sdk_signer.types.category.deserialize_json(
            data["category"]
        )
    if "signingConfiguration" in data:
        import aws_sdk_signer.types.signing_configuration

        out["signing_configuration"] = (
            aws_sdk_signer.types.signing_configuration.deserialize_json(
                data["signingConfiguration"]
            )
        )
    if "signingImageFormat" in data:
        import aws_sdk_signer.types.signing_image_format

        out["signing_image_format"] = (
            aws_sdk_signer.types.signing_image_format.deserialize_json(
                data["signingImageFormat"]
            )
        )
    if "maxSizeInMB" in data:
        out["max_size_in_mb"] = data["maxSizeInMB"]
    else:
        out["max_size_in_mb"] = 0
    if "revocationSupported" in data:
        out["revocation_supported"] = data["revocationSupported"]
    else:
        out["revocation_supported"] = False
    return out
