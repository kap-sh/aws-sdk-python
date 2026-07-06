"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SpekeKeyProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__string_pattern_arn_aws_us_gov_acm
    import aws_sdk_mediaconvert.types.__string_pattern_https_d
    import aws_sdk_mediaconvert.types.encryption_contract_configuration


class SpekeKeyProvider(TypedDict, closed=True):
    certificate_arn: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_arn_aws_us_gov_acm.__stringPatternArnAwsUsGovAcm"
    ]
    """If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificate's Amazon Resource Name (ARN) here."""
    encryption_contract_configuration: NotRequired[
        "aws_sdk_mediaconvert.types.encryption_contract_configuration.EncryptionContractConfiguration"
    ]
    """Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset."""
    resource_id: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Specify the resource ID that your SPEKE-compliant key provider uses to identify this content."""
    system_ids: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.__listOf__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12"
    ]
    """Relates to SPEKE implementation. DRM system identifiers. DASH output groups support a max of two system ids. HLS output groups support a max of 3 system ids. Other group types support one system id. See https://dashif.org/identifiers/content_protection/ for more details."""
    url: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_https_d.__stringPatternHttpsD"
    ]
    """Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content."""


# --- restJson1 ser/de ---
def serialize_json(value: SpekeKeyProvider) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "encryption_contract_configuration" in value:
        import aws_sdk_mediaconvert.types.encryption_contract_configuration

        out["encryptionContractConfiguration"] = (
            aws_sdk_mediaconvert.types.encryption_contract_configuration.serialize_json(
                value["encryption_contract_configuration"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "system_ids" in value:
        import aws_sdk_mediaconvert.types.__list_of__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12

        out["systemIds"] = (
            aws_sdk_mediaconvert.types.__list_of__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.serialize_json(
                value["system_ids"]
            )
        )
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SpekeKeyProvider:
    out: SpekeKeyProvider = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "encryptionContractConfiguration" in data:
        import aws_sdk_mediaconvert.types.encryption_contract_configuration

        out["encryption_contract_configuration"] = (
            aws_sdk_mediaconvert.types.encryption_contract_configuration.deserialize_json(
                data["encryptionContractConfiguration"]
            )
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "systemIds" in data:
        import aws_sdk_mediaconvert.types.__list_of__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12

        out["system_ids"] = (
            aws_sdk_mediaconvert.types.__list_of__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.deserialize_json(
                data["systemIds"]
            )
        )
    if "url" in data:
        out["url"] = data["url"]
    return out
