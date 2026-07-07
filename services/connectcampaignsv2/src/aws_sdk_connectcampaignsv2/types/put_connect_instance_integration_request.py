"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutConnectInstanceIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_id
    import aws_sdk_connectcampaignsv2.types.integration_config


class PutConnectInstanceIntegrationRequest(TypedDict, closed=True):
    connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"
    integration_config: (
        "aws_sdk_connectcampaignsv2.types.integration_config.IntegrationConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PutConnectInstanceIntegrationRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.integration_config

    out["integrationConfig"] = (
        aws_sdk_connectcampaignsv2.types.integration_config.serialize_json(
            value["integration_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutConnectInstanceIntegrationRequest:
    out: PutConnectInstanceIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "integrationConfig" in data:
        import aws_sdk_connectcampaignsv2.types.integration_config

        out["integration_config"] = (
            aws_sdk_connectcampaignsv2.types.integration_config.deserialize_json(
                data["integrationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "PutConnectInstanceIntegrationRequest.integration_config required"
        )
    return out
