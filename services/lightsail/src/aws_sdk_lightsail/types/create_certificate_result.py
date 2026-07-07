"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateCertificateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_summary
    import aws_sdk_lightsail.types.operation_list


class CreateCertificateResult(TypedDict, closed=True):
    certificate: NotRequired[
        "aws_sdk_lightsail.types.certificate_summary.CertificateSummary"
    ]
    """<p>An object that describes the certificate created.</p>"""
    operations: NotRequired["aws_sdk_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCertificateResult) -> dict:
    out: dict = {}
    if "certificate" in value:
        import aws_sdk_lightsail.types.certificate_summary

        out["certificate"] = (
            aws_sdk_lightsail.types.certificate_summary.serialize_aws_json_1_1(
                value["certificate"]
            )
        )
    if "operations" in value:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCertificateResult:
    out: CreateCertificateResult = {}  # type: ignore[typeddict-item]
    if "certificate" in data:
        import aws_sdk_lightsail.types.certificate_summary

        out["certificate"] = (
            aws_sdk_lightsail.types.certificate_summary.deserialize_aws_json_1_1(
                data["certificate"]
            )
        )
    if "operations" in data:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
