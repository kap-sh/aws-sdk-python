"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteConnectInstanceIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_id
    import aws_sdk_connectcampaignsv2.types.integration_identifier


class DeleteConnectInstanceIntegrationRequest(TypedDict, closed=True):
    connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"
    integration_identifier: (
        "aws_sdk_connectcampaignsv2.types.integration_identifier.IntegrationIdentifier"
    )


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectInstanceIntegrationRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.integration_identifier

    out["integrationIdentifier"] = (
        aws_sdk_connectcampaignsv2.types.integration_identifier.serialize_json(
            value["integration_identifier"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteConnectInstanceIntegrationRequest:
    out: DeleteConnectInstanceIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "integrationIdentifier" in data:
        import aws_sdk_connectcampaignsv2.types.integration_identifier

        out["integration_identifier"] = (
            aws_sdk_connectcampaignsv2.types.integration_identifier.deserialize_json(
                data["integrationIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteConnectInstanceIntegrationRequest.integration_identifier required"
        )
    return out
