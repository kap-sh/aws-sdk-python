"""Generated from Smithy shape ``com.amazonaws.workmail#TestAvailabilityConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.domain_name
    import aws_sdk_workmail.types.ews_availability_provider
    import aws_sdk_workmail.types.lambda_availability_provider
    import aws_sdk_workmail.types.organization_id


class TestAvailabilityConfigurationRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization where the availability provider will be tested.</p>"""
    domain_name: NotRequired["aws_sdk_workmail.types.domain_name.DomainName"]
    """<p>The domain to which the provider applies. If this field is provided, a stored availability provider associated to this domain name will be tested.</p>"""
    ews_provider: NotRequired[
        "aws_sdk_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
    ]
    lambda_provider: NotRequired[
        "aws_sdk_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestAvailabilityConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "domain_name" in value:
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


def deserialize_aws_json_1_1(data: dict) -> TestAvailabilityConfigurationRequest:
    out: TestAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "TestAvailabilityConfigurationRequest.organization_id required"
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
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
