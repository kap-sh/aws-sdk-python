"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#GetConnectInstanceConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.instance_config


class GetConnectInstanceConfigResponse(TypedDict, closed=True):
    connect_instance_config: NotRequired[
        "capo_connectcampaignsv2.types.instance_config.InstanceConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectInstanceConfigResponse) -> dict:
    out: dict = {}
    if "connect_instance_config" in value:
        import capo_connectcampaignsv2.types.instance_config

        out["connectInstanceConfig"] = (
            capo_connectcampaignsv2.types.instance_config.serialize_json(
                value["connect_instance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConnectInstanceConfigResponse:
    out: GetConnectInstanceConfigResponse = {}  # type: ignore[typeddict-item]
    if "connectInstanceConfig" in data:
        import capo_connectcampaignsv2.types.instance_config

        out["connect_instance_config"] = (
            capo_connectcampaignsv2.types.instance_config.deserialize_json(
                data["connectInstanceConfig"]
            )
        )
    return out
