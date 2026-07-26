"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#IntegrationSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.customer_profiles_integration_summary
    import capo_connectcampaignsv2.types.lambda_integration_summary
    import capo_connectcampaignsv2.types.q_connect_integration_summary


class _IntegrationSummary_customerProfiles(TypedDict, closed=True):
    customerProfiles: "capo_connectcampaignsv2.types.customer_profiles_integration_summary.CustomerProfilesIntegrationSummary"


class _IntegrationSummary_qConnect(TypedDict, closed=True):
    qConnect: "capo_connectcampaignsv2.types.q_connect_integration_summary.QConnectIntegrationSummary"


_IntegrationSummary_lambda = TypedDict(
    "_IntegrationSummary_lambda",
    {
        "lambda": "capo_connectcampaignsv2.types.lambda_integration_summary.LambdaIntegrationSummary",
    },
    closed=True,
)

IntegrationSummary: TypeAlias = (
    _IntegrationSummary_customerProfiles
    | _IntegrationSummary_qConnect
    | _IntegrationSummary_lambda
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummary) -> dict:
    if "customerProfiles" in value:
        import capo_connectcampaignsv2.types.customer_profiles_integration_summary

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_summary.serialize_json(
                value["customerProfiles"]
            )
        }
    elif "qConnect" in value:
        import capo_connectcampaignsv2.types.q_connect_integration_summary

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_summary.serialize_json(
                value["qConnect"]
            )
        }
    elif "lambda" in value:
        import capo_connectcampaignsv2.types.lambda_integration_summary

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_summary.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("IntegrationSummary: no variant present")


def deserialize_json(data: dict) -> IntegrationSummary:
    if "customerProfiles" in data:
        import capo_connectcampaignsv2.types.customer_profiles_integration_summary

        return {
            "customerProfiles": capo_connectcampaignsv2.types.customer_profiles_integration_summary.deserialize_json(
                data["customerProfiles"]
            )
        }
    elif "qConnect" in data:
        import capo_connectcampaignsv2.types.q_connect_integration_summary

        return {
            "qConnect": capo_connectcampaignsv2.types.q_connect_integration_summary.deserialize_json(
                data["qConnect"]
            )
        }
    elif "lambda" in data:
        import capo_connectcampaignsv2.types.lambda_integration_summary

        return {
            "lambda": capo_connectcampaignsv2.types.lambda_integration_summary.deserialize_json(
                data["lambda"]
            )
        }
    else:
        raise DeserializationError("IntegrationSummary: no recognized variant key")
