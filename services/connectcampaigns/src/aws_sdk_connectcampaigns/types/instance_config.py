"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#InstanceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.encryption_config
    import aws_sdk_connectcampaigns.types.instance_id
    import aws_sdk_connectcampaigns.types.service_linked_role_arn


class InstanceConfig(TypedDict):
    connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId"
    service_linked_role_arn: (
        "aws_sdk_connectcampaigns.types.service_linked_role_arn.ServiceLinkedRoleArn"
    )
    encryption_config: (
        "aws_sdk_connectcampaigns.types.encryption_config.EncryptionConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: InstanceConfig) -> dict:
    out: dict = {}
    out["connectInstanceId"] = value["connect_instance_id"]
    out["serviceLinkedRoleArn"] = value["service_linked_role_arn"]
    import aws_sdk_connectcampaigns.types.encryption_config

    out["encryptionConfig"] = (
        aws_sdk_connectcampaigns.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> InstanceConfig:
    out: InstanceConfig = {}  # type: ignore[typeddict-item]
    if "connectInstanceId" in data:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        raise DeserializationError("InstanceConfig.connect_instance_id required")
    if "serviceLinkedRoleArn" in data:
        out["service_linked_role_arn"] = data["serviceLinkedRoleArn"]
    else:
        raise DeserializationError("InstanceConfig.service_linked_role_arn required")
    if "encryptionConfig" in data:
        import aws_sdk_connectcampaigns.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_connectcampaigns.types.encryption_config.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        raise DeserializationError("InstanceConfig.encryption_config required")
    return out
