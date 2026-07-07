"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateAvailabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.domain_name
    import aws_sdk_workmail.types.ews_availability_provider
    import aws_sdk_workmail.types.lambda_availability_provider
    import aws_sdk_workmail.types.organization_id


class UpdateAvailabilityConfigurationRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be updated.</p>"""
    domain_name: "aws_sdk_workmail.types.domain_name.DomainName"
    """<p>The domain to which the provider applies the availability configuration.</p>"""
    ews_provider: NotRequired[
        "aws_sdk_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
    ]
    """<p>The EWS availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>. The previously stored provider will be overridden by the one provided.</p>"""
    lambda_provider: NotRequired[
        "aws_sdk_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
    ]
    """<p>The Lambda availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>. The previously stored provider will be overridden by the one provided.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAvailabilityConfigurationRequest) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> UpdateAvailabilityConfigurationRequest:
    out: UpdateAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "UpdateAvailabilityConfigurationRequest.organization_id required"
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "UpdateAvailabilityConfigurationRequest.domain_name required"
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
