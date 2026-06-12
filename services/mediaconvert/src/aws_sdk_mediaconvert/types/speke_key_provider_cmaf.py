"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SpekeKeyProviderCmaf``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12
    import aws_sdk_mediaconvert.types.__string_pattern_arn_aws_us_gov_acm
    import aws_sdk_mediaconvert.types.__string_pattern_https_d
    import aws_sdk_mediaconvert.types.__string_pattern_w
    import aws_sdk_mediaconvert.types.encryption_contract_configuration


class SpekeKeyProviderCmaf(TypedDict):
    certificate_arn: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_arn_aws_us_gov_acm.__stringPatternArnAwsUsGovAcm"
    ]
    """If you want your key provider to encrypt the content keys that it provides to MediaConvert, set up a certificate with a master key using AWS Certificate Manager. Specify the certificate's Amazon Resource Name (ARN) here."""
    dash_signaled_system_ids: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.__listOf__stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12"
    ]
    """Specify the DRM system IDs that you want signaled in the DASH manifest that MediaConvert creates as part of this CMAF package. The DASH manifest can currently signal up to three system IDs. For more information, see https://dashif.org/identifiers/content_protection/."""
    encryption_contract_configuration: NotRequired[
        "aws_sdk_mediaconvert.types.encryption_contract_configuration.EncryptionContractConfiguration"
    ]
    """Specify the SPEKE version, either v1.0 or v2.0, that MediaConvert uses when encrypting your output. For more information, see: https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html To use SPEKE v1.0: Leave blank. To use SPEKE v2.0: Specify a SPEKE v2.0 video preset and a SPEKE v2.0 audio preset."""
    hls_signaled_system_ids: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.__listOf__stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12"
    ]
    """Specify up to 3 DRM system IDs that you want signaled in the HLS manifest that MediaConvert creates as part of this CMAF package. For more information, see https://dashif.org/identifiers/content_protection/."""
    resource_id: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_w.__stringPatternW"
    ]
    """Specify the resource ID that your SPEKE-compliant key provider uses to identify this content."""
    url: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_https_d.__stringPatternHttpsD"
    ]
    """Specify the URL to the key server that your SPEKE-compliant DRM key provider uses to provide keys for encrypting your content."""


# --- restJson1 ser/de ---
def serialize_json(value: SpekeKeyProviderCmaf) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "dash_signaled_system_ids" in value:
        import aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12

        out["dashSignaledSystemIds"] = (
            aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.serialize_json(
                value["dash_signaled_system_ids"]
            )
        )
    if "encryption_contract_configuration" in value:
        import aws_sdk_mediaconvert.types.encryption_contract_configuration

        out["encryptionContractConfiguration"] = (
            aws_sdk_mediaconvert.types.encryption_contract_configuration.serialize_json(
                value["encryption_contract_configuration"]
            )
        )
    if "hls_signaled_system_ids" in value:
        import aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12

        out["hlsSignaledSystemIds"] = (
            aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.serialize_json(
                value["hls_signaled_system_ids"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SpekeKeyProviderCmaf:
    out: SpekeKeyProviderCmaf = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "dashSignaledSystemIds" in data:
        import aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12

        out["dash_signaled_system_ids"] = (
            aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.deserialize_json(
                data["dashSignaledSystemIds"]
            )
        )
    if "encryptionContractConfiguration" in data:
        import aws_sdk_mediaconvert.types.encryption_contract_configuration

        out["encryption_contract_configuration"] = (
            aws_sdk_mediaconvert.types.encryption_contract_configuration.deserialize_json(
                data["encryptionContractConfiguration"]
            )
        )
    if "hlsSignaledSystemIds" in data:
        import aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12

        out["hls_signaled_system_ids"] = (
            aws_sdk_mediaconvert.types.__list_of__string_min36_max36_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.deserialize_json(
                data["hlsSignaledSystemIds"]
            )
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "url" in data:
        out["url"] = data["url"]
    return out
