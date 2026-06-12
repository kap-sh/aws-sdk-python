"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutInstanceCommunicationLimitsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_communication_limits_config
    import aws_sdk_connectcampaignsv2.types.instance_id


class PutInstanceCommunicationLimitsRequest(TypedDict):
    connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"
    communication_limits_config: "aws_sdk_connectcampaignsv2.types.instance_communication_limits_config.InstanceCommunicationLimitsConfig"


# --- restJson1 ser/de ---
def serialize_json(value: PutInstanceCommunicationLimitsRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.instance_communication_limits_config

    out["communicationLimitsConfig"] = (
        aws_sdk_connectcampaignsv2.types.instance_communication_limits_config.serialize_json(
            value["communication_limits_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutInstanceCommunicationLimitsRequest:
    out: PutInstanceCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
    if "communicationLimitsConfig" in data:
        import aws_sdk_connectcampaignsv2.types.instance_communication_limits_config

        out["communication_limits_config"] = (
            aws_sdk_connectcampaignsv2.types.instance_communication_limits_config.deserialize_json(
                data["communicationLimitsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "PutInstanceCommunicationLimitsRequest.communication_limits_config required"
        )
    return out
