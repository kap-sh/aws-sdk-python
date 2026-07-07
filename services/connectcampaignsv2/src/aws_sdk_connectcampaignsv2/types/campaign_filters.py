"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CampaignFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_id_filter


class CampaignFilters(TypedDict, closed=True):
    instance_id_filter: NotRequired[
        "aws_sdk_connectcampaignsv2.types.instance_id_filter.InstanceIdFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CampaignFilters) -> dict:
    out: dict = {}
    if "instance_id_filter" in value:
        import aws_sdk_connectcampaignsv2.types.instance_id_filter

        out["instanceIdFilter"] = (
            aws_sdk_connectcampaignsv2.types.instance_id_filter.serialize_json(
                value["instance_id_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> CampaignFilters:
    out: CampaignFilters = {}  # type: ignore[typeddict-item]
    if "instanceIdFilter" in data:
        import aws_sdk_connectcampaignsv2.types.instance_id_filter

        out["instance_id_filter"] = (
            aws_sdk_connectcampaignsv2.types.instance_id_filter.deserialize_json(
                data["instanceIdFilter"]
            )
        )
    return out
