"""Generated from Smithy shape ``com.amazonaws.workmail#CreateAvailabilityConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.domain_name
    import aws_sdk_workmail.types.ews_availability_provider
    import aws_sdk_workmail.types.idempotency_client_token
    import aws_sdk_workmail.types.lambda_availability_provider
    import aws_sdk_workmail.types.organization_id


class CreateAvailabilityConfigurationRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>An idempotent token that ensures that an API request is executed only once.</p>"""
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be created.</p>"""
    domain_name: "aws_sdk_workmail.types.domain_name.DomainName"
    """<p>The domain to which the provider applies.</p>"""
    ews_provider: NotRequired[
        "aws_sdk_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
    ]
    """<p>Exchange Web Services (EWS) availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>.</p>"""
    lambda_provider: NotRequired[
        "aws_sdk_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
    ]
    """<p>Lambda availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAvailabilityConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    if "ews_provider" in value:
        import aws_sdk_workmail.types.ews_availability_provider

        out["EwsProvider"] = (
            aws_sdk_workmail.types.ews_availability_provider.serialize_aws_json_1_1(
                value["ews_provider"]
            )
        )
    if "lambda_provider" in value:
        import aws_sdk_workmail.types.lambda_availability_provider

        out["LambdaProvider"] = (
            aws_sdk_workmail.types.lambda_availability_provider.serialize_aws_json_1_1(
                value["lambda_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAvailabilityConfigurationRequest:
    out: CreateAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "CreateAvailabilityConfigurationRequest.organization_id required"
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "CreateAvailabilityConfigurationRequest.domain_name required"
        )
    if "EwsProvider" in data:
        import aws_sdk_workmail.types.ews_availability_provider

        out["ews_provider"] = (
            aws_sdk_workmail.types.ews_availability_provider.deserialize_aws_json_1_1(
                data["EwsProvider"]
            )
        )
    if "LambdaProvider" in data:
        import aws_sdk_workmail.types.lambda_availability_provider

        out["lambda_provider"] = (
            aws_sdk_workmail.types.lambda_availability_provider.deserialize_aws_json_1_1(
                data["LambdaProvider"]
            )
        )
    return out
