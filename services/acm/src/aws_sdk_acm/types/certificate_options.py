"""Generated from Smithy shape ``com.amazonaws.acm#CertificateOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_export
    import aws_sdk_acm.types.certificate_transparency_logging_preference


class CertificateOptions(TypedDict, closed=True):
    certificate_transparency_logging_preference: NotRequired[
        "aws_sdk_acm.types.certificate_transparency_logging_preference.CertificateTransparencyLoggingPreference"
    ]
    """<p>You can opt out of certificate transparency logging by specifying the <code>DISABLED</code> option. Opt in by specifying <code>ENABLED</code>. </p>"""
    export: NotRequired["aws_sdk_acm.types.certificate_export.CertificateExport"]
    """<p>You can opt in to allow the export of your certificates by specifying <code>ENABLED</code>. You cannot update the value of <code>Export</code> after the the certificate is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateOptions) -> dict:
    out: dict = {}
    if "certificate_transparency_logging_preference" in value:
        import aws_sdk_acm.types.certificate_transparency_logging_preference

        out["CertificateTransparencyLoggingPreference"] = (
            aws_sdk_acm.types.certificate_transparency_logging_preference.serialize_aws_json_1_1(
                value["certificate_transparency_logging_preference"]
            )
        )
    if "export" in value:
        import aws_sdk_acm.types.certificate_export

        out["Export"] = aws_sdk_acm.types.certificate_export.serialize_aws_json_1_1(
            value["export"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateOptions:
    out: CertificateOptions = {}  # type: ignore[typeddict-item]
    if "CertificateTransparencyLoggingPreference" in data:
        import aws_sdk_acm.types.certificate_transparency_logging_preference

        out["certificate_transparency_logging_preference"] = (
            aws_sdk_acm.types.certificate_transparency_logging_preference.deserialize_aws_json_1_1(
                data["CertificateTransparencyLoggingPreference"]
            )
        )
    if "Export" in data:
        import aws_sdk_acm.types.certificate_export

        out["export"] = aws_sdk_acm.types.certificate_export.deserialize_aws_json_1_1(
            data["Export"]
        )
    return out
