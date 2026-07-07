"""Generated from Smithy shape ``com.amazonaws.workmail#AvailabilityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.availability_provider_type
    import aws_sdk_workmail.types.domain_name
    import aws_sdk_workmail.types.lambda_availability_provider
    import aws_sdk_workmail.types.redacted_ews_availability_provider
    import aws_sdk_workmail.types.timestamp


class AvailabilityConfiguration(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_workmail.types.domain_name.DomainName"]
    """<p>Displays the domain to which the provider applies.</p>"""
    provider_type: NotRequired[
        "aws_sdk_workmail.types.availability_provider_type.AvailabilityProviderType"
    ]
    """<p>Displays the provider type that applies to this domain.</p>"""
    ews_provider: NotRequired[
        "aws_sdk_workmail.types.redacted_ews_availability_provider.RedactedEwsAvailabilityProvider"
    ]
    """<p>If <code>ProviderType</code> is <code>EWS</code>, then this field contains <code>RedactedEwsAvailabilityProvider</code>. Otherwise, it is not required.</p>"""
    lambda_provider: NotRequired[
        "aws_sdk_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
    ]
    """<p>If ProviderType is <code>LAMBDA</code> then this field contains <code>LambdaAvailabilityProvider</code>. Otherwise, it is not required.</p>"""
    date_created: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which the availability configuration was created.</p>"""
    date_modified: NotRequired["aws_sdk_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which the availability configuration was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityConfiguration) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "provider_type" in value:
        import aws_sdk_workmail.types.availability_provider_type

        out["ProviderType"] = (
            aws_sdk_workmail.types.availability_provider_type.serialize_aws_json_1_1(
                value["provider_type"]
            )
        )
    if "ews_provider" in value:
        import aws_sdk_workmail.types.redacted_ews_availability_provider

        out["EwsProvider"] = (
            aws_sdk_workmail.types.redacted_ews_availability_provider.serialize_aws_json_1_1(
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
    if "date_created" in value:
        import aws_sdk_workmail.types.timestamp

        out["DateCreated"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_modified" in value:
        import aws_sdk_workmail.types.timestamp

        out["DateModified"] = aws_sdk_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_modified"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AvailabilityConfiguration:
    out: AvailabilityConfiguration = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "ProviderType" in data:
        import aws_sdk_workmail.types.availability_provider_type

        out["provider_type"] = (
            aws_sdk_workmail.types.availability_provider_type.deserialize_aws_json_1_1(
                data["ProviderType"]
            )
        )
    if "EwsProvider" in data:
        import aws_sdk_workmail.types.redacted_ews_availability_provider

        out["ews_provider"] = (
            aws_sdk_workmail.types.redacted_ews_availability_provider.deserialize_aws_json_1_1(
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
    if "DateCreated" in data:
        import aws_sdk_workmail.types.timestamp

        out["date_created"] = aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateModified" in data:
        import aws_sdk_workmail.types.timestamp

        out["date_modified"] = (
            aws_sdk_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["DateModified"]
            )
        )
    return out
