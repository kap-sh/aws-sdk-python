"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#RestrictedPeriodList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.restricted_period

RestrictedPeriodList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.restricted_period.RestrictedPeriod"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestrictedPeriodList) -> list:
    import aws_sdk_connectcampaignsv2.types.restricted_period

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcampaignsv2.types.restricted_period.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RestrictedPeriodList:
    import aws_sdk_connectcampaignsv2.types.restricted_period

    out: RestrictedPeriodList = []
    for item in data:
        out.append(
            aws_sdk_connectcampaignsv2.types.restricted_period.deserialize_json(item)
        )
    return out
