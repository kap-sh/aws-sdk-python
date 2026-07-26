"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#RestrictedPeriodList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.restricted_period

RestrictedPeriodList: TypeAlias = list[
    "capo_connectcampaignsv2.types.restricted_period.RestrictedPeriod"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestrictedPeriodList) -> list:
    import capo_connectcampaignsv2.types.restricted_period

    out: list = []
    for item in value:
        out.append(capo_connectcampaignsv2.types.restricted_period.serialize_json(item))
    return out


def deserialize_json(data: list) -> RestrictedPeriodList:
    import capo_connectcampaignsv2.types.restricted_period

    out: RestrictedPeriodList = []
    for item in data:
        out.append(
            capo_connectcampaignsv2.types.restricted_period.deserialize_json(item)
        )
    return out
