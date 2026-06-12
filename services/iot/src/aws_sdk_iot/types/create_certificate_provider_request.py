"""Generated from Smithy shape ``com.amazonaws.iot#CreateCertificateProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_provider_account_default_for_operations
    import aws_sdk_iot.types.certificate_provider_function_arn
    import aws_sdk_iot.types.certificate_provider_name
    import aws_sdk_iot.types.client_token
    import aws_sdk_iot.types.tag_list


class CreateCertificateProviderRequest(TypedDict):
    certificate_provider_name: (
        "aws_sdk_iot.types.certificate_provider_name.CertificateProviderName"
    )
    """<p>The name of the certificate provider.</p>"""
    lambda_function_arn: "aws_sdk_iot.types.certificate_provider_function_arn.CertificateProviderFunctionArn"
    """<p>The ARN of the Lambda function that defines the authentication logic.</p>"""
    account_default_for_operations: "aws_sdk_iot.types.certificate_provider_account_default_for_operations.CertificateProviderAccountDefaultForOperations"
    """<p>A list of the operations that the certificate provider will use to generate certificates. Valid value: <code>CreateCertificateFromCsr</code>.</p>"""
    client_token: NotRequired["aws_sdk_iot.types.client_token.ClientToken"]
    """<p>A string that you can optionally pass in the <code>CreateCertificateProvider</code> request to make sure the request is idempotent.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the certificate provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCertificateProviderRequest) -> dict:
    out: dict = {}
    out["lambdaFunctionArn"] = value["lambda_function_arn"]
    import aws_sdk_iot.types.certificate_provider_account_default_for_operations

    out["accountDefaultForOperations"] = (
        aws_sdk_iot.types.certificate_provider_account_default_for_operations.serialize_json(
            value["account_default_for_operations"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCertificateProviderRequest:
    out: CreateCertificateProviderRequest = {}  # type: ignore[typeddict-item]
    if "lambdaFunctionArn" in data:
        out["lambda_function_arn"] = data["lambdaFunctionArn"]
    else:
        raise DeserializationError(
            "CreateCertificateProviderRequest.lambda_function_arn required"
        )
    if "accountDefaultForOperations" in data:
        import aws_sdk_iot.types.certificate_provider_account_default_for_operations

        out["account_default_for_operations"] = (
            aws_sdk_iot.types.certificate_provider_account_default_for_operations.deserialize_json(
                data["accountDefaultForOperations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCertificateProviderRequest.account_default_for_operations required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    return out
