"""Generated from Smithy shape ``com.amazonaws.iot#DescribeCertificateProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_provider_account_default_for_operations
    import aws_sdk_iot.types.certificate_provider_arn
    import aws_sdk_iot.types.certificate_provider_function_arn
    import aws_sdk_iot.types.certificate_provider_name
    import aws_sdk_iot.types.date_type


class DescribeCertificateProviderResponse(TypedDict, closed=True):
    certificate_provider_name: NotRequired[
        "aws_sdk_iot.types.certificate_provider_name.CertificateProviderName"
    ]
    """<p>The name of the certificate provider.</p>"""
    certificate_provider_arn: NotRequired[
        "aws_sdk_iot.types.certificate_provider_arn.CertificateProviderArn"
    ]
    """<p>The ARN of the certificate provider.</p>"""
    lambda_function_arn: NotRequired[
        "aws_sdk_iot.types.certificate_provider_function_arn.CertificateProviderFunctionArn"
    ]
    """<p>The Lambda function ARN that's associated with the certificate provider.</p>"""
    account_default_for_operations: NotRequired[
        "aws_sdk_iot.types.certificate_provider_account_default_for_operations.CertificateProviderAccountDefaultForOperations"
    ]
    """<p>A list of the operations that the certificate provider will use to generate certificates. Valid value: <code>CreateCertificateFromCsr</code>.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date-time string that indicates when the certificate provider was created.</p>"""
    last_modified_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date-time string that indicates when the certificate provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCertificateProviderResponse) -> dict:
    out: dict = {}
    if "certificate_provider_name" in value:
        out["certificateProviderName"] = value["certificate_provider_name"]
    if "certificate_provider_arn" in value:
        out["certificateProviderArn"] = value["certificate_provider_arn"]
    if "lambda_function_arn" in value:
        out["lambdaFunctionArn"] = value["lambda_function_arn"]
    if "account_default_for_operations" in value:
        import aws_sdk_iot.types.certificate_provider_account_default_for_operations

        out["accountDefaultForOperations"] = (
            aws_sdk_iot.types.certificate_provider_account_default_for_operations.serialize_json(
                value["account_default_for_operations"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.date_type

        out["lastModifiedDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCertificateProviderResponse:
    out: DescribeCertificateProviderResponse = {}  # type: ignore[typeddict-item]
    if "certificateProviderName" in data:
        out["certificate_provider_name"] = data["certificateProviderName"]
    if "certificateProviderArn" in data:
        out["certificate_provider_arn"] = data["certificateProviderArn"]
    if "lambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    if "accountDefaultForOperations" in data:
        import aws_sdk_iot.types.certificate_provider_account_default_for_operations

        out["account_default_for_operations"] = (
            aws_sdk_iot.types.certificate_provider_account_default_for_operations.deserialize_json(
                data["accountDefaultForOperations"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.date_type

        out["last_modified_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    return out
