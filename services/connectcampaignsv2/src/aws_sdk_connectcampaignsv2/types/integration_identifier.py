"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#IntegrationIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.customer_profiles_integration_identifier
    import aws_sdk_connectcampaignsv2.types.lambda_integration_identifier
    import aws_sdk_connectcampaignsv2.types.q_connect_integration_identifier


class _IntegrationIdentifier_customerProfiles(TypedDict):
    customerProfiles: "aws_sdk_connectcampaignsv2.types.customer_profiles_integration_identifier.CustomerProfilesIntegrationIdentifier"


class _IntegrationIdentifier_qConnect(TypedDict):
    qConnect: "aws_sdk_connectcampaignsv2.types.q_connect_integration_identifier.QConnectIntegrationIdentifier"


class _IntegrationIdentifier_lambda(TypedDict):
    lambda: (
        "aws_sdk_connectcampaignsv2.types.lambda_integration_identifier.LambdaIntegrationIdentifier"
    )


IntegrationIdentifier: TypeAlias = (
    _IntegrationIdentifier_customerProfiles
    | _IntegrationIdentifier_qConnect
    | _IntegrationIdentifier_lambda
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationIdentifier) -> dict:
    if "customerProfiles" in value:
        import aws_sdk_connectcampaignsv2.types.customer_profiles_integration_identifier

        return {
            "customerProfiles": aws_sdk_connectcampaignsv2.types.customer_profiles_integration_identifier.serialize_json(
                value["customerProfiles"]
            )
        }
    elif "qConnect" in value:
        import aws_sdk_connectcampaignsv2.types.q_connect_integration_identifier

        return {
            "qConnect": aws_sdk_connectcampaignsv2.types.q_connect_integration_identifier.serialize_json(
                value["qConnect"]
            )
        }
    elif "lambda" in value:
        import aws_sdk_connectcampaignsv2.types.lambda_integration_identifier

        return {
            "lambda": aws_sdk_connectcampaignsv2.types.lambda_integration_identifier.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("IntegrationIdentifier: no variant present")


def deserialize_json(data: dict) -> IntegrationIdentifier:
    if "customerProfiles" in data:
        import aws_sdk_connectcampaignsv2.types.customer_profiles_integration_identifier

        return {
            "customerProfiles": aws_sdk_connectcampaignsv2.types.customer_profiles_integration_identifier.deserialize_json(
                data["customerProfiles"]
            )
        }
    elif "qConnect" in data:
        import aws_sdk_connectcampaignsv2.types.q_connect_integration_identifier

        return {
            "qConnect": aws_sdk_connectcampaignsv2.types.q_connect_integration_identifier.deserialize_json(
                data["qConnect"]
            )
        }
    elif "lambda" in data:
        import aws_sdk_connectcampaignsv2.types.lambda_integration_identifier

        return {
            "lambda": aws_sdk_connectcampaignsv2.types.lambda_integration_identifier.deserialize_json(
                data["lambda"]
            )
        }
    else:
        raise DeserializationError("IntegrationIdentifier: no recognized variant key")
