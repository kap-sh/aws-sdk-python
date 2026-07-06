"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCertificateProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_provider_account_default_for_operations
    import aws_sdk_iot.types.certificate_provider_function_arn
    import aws_sdk_iot.types.certificate_provider_name


class UpdateCertificateProviderRequest(TypedDict, closed=True):
    certificate_provider_name: (
        "aws_sdk_iot.types.certificate_provider_name.CertificateProviderName"
    )
    """<p>The name of the certificate provider.</p>"""
    lambda_function_arn: NotRequired[
        "aws_sdk_iot.types.certificate_provider_function_arn.CertificateProviderFunctionArn"
    ]
    """<p>The Lambda function ARN that's associated with the certificate provider.</p>"""
    account_default_for_operations: NotRequired[
        "aws_sdk_iot.types.certificate_provider_account_default_for_operations.CertificateProviderAccountDefaultForOperations"
    ]
    """<p>A list of the operations that the certificate provider will use to generate certificates. Valid value: <code>CreateCertificateFromCsr</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCertificateProviderRequest) -> dict:
    out: dict = {}
    if "lambda_function_arn" in value:
        out["lambdaFunctionArn"] = value["lambda_function_arn"]
    if "account_default_for_operations" in value:
        import aws_sdk_iot.types.certificate_provider_account_default_for_operations

        out["accountDefaultForOperations"] = (
            aws_sdk_iot.types.certificate_provider_account_default_for_operations.serialize_json(
                value["account_default_for_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCertificateProviderRequest:
    out: UpdateCertificateProviderRequest = {}  # type: ignore[typeddict-item]
    if "lambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    if "accountDefaultForOperations" in data:
        import aws_sdk_iot.types.certificate_provider_account_default_for_operations

        out["account_default_for_operations"] = (
            aws_sdk_iot.types.certificate_provider_account_default_for_operations.deserialize_json(
                data["accountDefaultForOperations"]
            )
        )
    return out
