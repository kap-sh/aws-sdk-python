"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateDomainAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.auto_sub_domain_creation_patterns
    import aws_sdk_amplify.types.auto_sub_domain_iam_role
    import aws_sdk_amplify.types.certificate_settings
    import aws_sdk_amplify.types.domain_name
    import aws_sdk_amplify.types.enable_auto_sub_domain
    import aws_sdk_amplify.types.sub_domain_settings


class UpdateDomainAssociationRequest(TypedDict):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    domain_name: "aws_sdk_amplify.types.domain_name.DomainName"
    """<p> The name of the domain. </p>"""
    enable_auto_sub_domain: NotRequired[
        "aws_sdk_amplify.types.enable_auto_sub_domain.EnableAutoSubDomain"
    ]
    """<p> Enables the automated creation of subdomains for branches. </p>"""
    sub_domain_settings: NotRequired[
        "aws_sdk_amplify.types.sub_domain_settings.SubDomainSettings"
    ]
    """<p> Describes the settings for the subdomain. </p>"""
    auto_sub_domain_creation_patterns: NotRequired[
        "aws_sdk_amplify.types.auto_sub_domain_creation_patterns.AutoSubDomainCreationPatterns"
    ]
    """<p> Sets the branch patterns for automatic subdomain creation. </p>"""
    auto_sub_domain_iam_role: NotRequired[
        "aws_sdk_amplify.types.auto_sub_domain_iam_role.AutoSubDomainIAMRole"
    ]
    """<p> The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains. </p>"""
    certificate_settings: NotRequired[
        "aws_sdk_amplify.types.certificate_settings.CertificateSettings"
    ]
    """<p>The type of SSL/TLS certificate to use for your custom domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainAssociationRequest) -> dict:
    out: dict = {}
    if "enable_auto_sub_domain" in value:
        out["enableAutoSubDomain"] = value["enable_auto_sub_domain"]
    if "sub_domain_settings" in value:
        import aws_sdk_amplify.types.sub_domain_settings

        out["subDomainSettings"] = (
            aws_sdk_amplify.types.sub_domain_settings.serialize_json(
                value["sub_domain_settings"]
            )
        )
    if "auto_sub_domain_creation_patterns" in value:
        import aws_sdk_amplify.types.auto_sub_domain_creation_patterns

        out["autoSubDomainCreationPatterns"] = (
            aws_sdk_amplify.types.auto_sub_domain_creation_patterns.serialize_json(
                value["auto_sub_domain_creation_patterns"]
            )
        )
    if "auto_sub_domain_iam_role" in value:
        out["autoSubDomainIAMRole"] = value["auto_sub_domain_iam_role"]
    if "certificate_settings" in value:
        import aws_sdk_amplify.types.certificate_settings

        out["certificateSettings"] = (
            aws_sdk_amplify.types.certificate_settings.serialize_json(
                value["certificate_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDomainAssociationRequest:
    out: UpdateDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if "enableAutoSubDomain" in data:
        out["enable_auto_sub_domain"] = data["enableAutoSubDomain"]
    if "subDomainSettings" in data:
        import aws_sdk_amplify.types.sub_domain_settings

        out["sub_domain_settings"] = (
            aws_sdk_amplify.types.sub_domain_settings.deserialize_json(
                data["subDomainSettings"]
            )
        )
    if "autoSubDomainCreationPatterns" in data:
        import aws_sdk_amplify.types.auto_sub_domain_creation_patterns

        out["auto_sub_domain_creation_patterns"] = (
            aws_sdk_amplify.types.auto_sub_domain_creation_patterns.deserialize_json(
                data["autoSubDomainCreationPatterns"]
            )
        )
    if "autoSubDomainIAMRole" in data:
        out["auto_sub_domain_iam_role"] = data["autoSubDomainIAMRole"]
    if "certificateSettings" in data:
        import aws_sdk_amplify.types.certificate_settings

        out["certificate_settings"] = (
            aws_sdk_amplify.types.certificate_settings.deserialize_json(
                data["certificateSettings"]
            )
        )
    return out
