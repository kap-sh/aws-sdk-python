"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#IntegrationSummary``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.customer_profiles_integration_summary
    import aws_sdk_connectcampaignsv2.types.lambda_integration_summary
    import aws_sdk_connectcampaignsv2.types.q_connect_integration_summary


class _IntegrationSummary_customerProfiles(TypedDict):
    customerProfiles: "aws_sdk_connectcampaignsv2.types.customer_profiles_integration_summary.CustomerProfilesIntegrationSummary"


class _IntegrationSummary_qConnect(TypedDict):
    qConnect: "aws_sdk_connectcampaignsv2.types.q_connect_integration_summary.QConnectIntegrationSummary"


_IntegrationSummary_lambda = TypedDict(
    "_IntegrationSummary_lambda",
    {
        "lambda": "aws_sdk_connectcampaignsv2.types.lambda_integration_summary.LambdaIntegrationSummary",
    },
)

IntegrationSummary: TypeAlias = (
    _IntegrationSummary_customerProfiles
    | _IntegrationSummary_qConnect
    | _IntegrationSummary_lambda
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummary) -> dict:
    if "customerProfiles" in value:
        import aws_sdk_connectcampaignsv2.types.customer_profiles_integration_summary

        return {
            "customerProfiles": aws_sdk_connectcampaignsv2.types.customer_profiles_integration_summary.serialize_json(
                value["customerProfiles"]
            )
        }
    elif "qConnect" in value:
        import aws_sdk_connectcampaignsv2.types.q_connect_integration_summary

        return {
            "qConnect": aws_sdk_connectcampaignsv2.types.q_connect_integration_summary.serialize_json(
                value["qConnect"]
            )
        }
    elif "lambda" in value:
        import aws_sdk_connectcampaignsv2.types.lambda_integration_summary

        return {
            "lambda": aws_sdk_connectcampaignsv2.types.lambda_integration_summary.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("IntegrationSummary: no variant present")


def deserialize_json(data: dict) -> IntegrationSummary:
    if "customerProfiles" in data:
        import aws_sdk_connectcampaignsv2.types.customer_profiles_integration_summary

        return {
            "customerProfiles": aws_sdk_connectcampaignsv2.types.customer_profiles_integration_summary.deserialize_json(
                data["customerProfiles"]
            )
        }
    elif "qConnect" in data:
        import aws_sdk_connectcampaignsv2.types.q_connect_integration_summary

        return {
            "qConnect": aws_sdk_connectcampaignsv2.types.q_connect_integration_summary.deserialize_json(
                data["qConnect"]
            )
        }
    elif "lambda" in data:
        import aws_sdk_connectcampaignsv2.types.lambda_integration_summary

        return {
            "lambda": aws_sdk_connectcampaignsv2.types.lambda_integration_summary.deserialize_json(
                data["lambda"]
            )
        }
    else:
        raise DeserializationError("IntegrationSummary: no recognized variant key")
