"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#InstanceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.encryption_config
    import capo_connectcampaignsv2.types.instance_id
    import capo_connectcampaignsv2.types.service_linked_role_arn


class InstanceConfig(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaignsv2.types.instance_id.InstanceId"
    service_linked_role_arn: (
        "capo_connectcampaignsv2.types.service_linked_role_arn.ServiceLinkedRoleArn"
    )
    encryption_config: (
        "capo_connectcampaignsv2.types.encryption_config.EncryptionConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: InstanceConfig) -> dict:
    out: dict = {}
    out["connectInstanceId"] = value["connect_instance_id"]
    out["serviceLinkedRoleArn"] = value["service_linked_role_arn"]
    import capo_connectcampaignsv2.types.encryption_config

    out["encryptionConfig"] = (
        capo_connectcampaignsv2.types.encryption_config.serialize_json(
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
        import capo_connectcampaignsv2.types.encryption_config

        out["encryption_config"] = (
            capo_connectcampaignsv2.types.encryption_config.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        raise DeserializationError("InstanceConfig.encryption_config required")
    return out
