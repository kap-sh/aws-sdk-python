"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#RestrictedPeriods``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.restricted_period_list


class _RestrictedPeriods_restrictedPeriodList(TypedDict, closed=True):
    restrictedPeriodList: (
        "capo_connectcampaignsv2.types.restricted_period_list.RestrictedPeriodList"
    )


RestrictedPeriods: TypeAlias = _RestrictedPeriods_restrictedPeriodList


# --- restJson1 ser/de ---
def serialize_json(value: RestrictedPeriods) -> dict:
    if "restrictedPeriodList" in value:
        import capo_connectcampaignsv2.types.restricted_period_list

        return {
            "restrictedPeriodList": capo_connectcampaignsv2.types.restricted_period_list.serialize_json(
                value["restrictedPeriodList"]
            )
        }
    else:
        raise SerializationError("RestrictedPeriods: no variant present")


def deserialize_json(data: dict) -> RestrictedPeriods:
    if "restrictedPeriodList" in data:
        import capo_connectcampaignsv2.types.restricted_period_list

        return {
            "restrictedPeriodList": capo_connectcampaignsv2.types.restricted_period_list.deserialize_json(
                data["restrictedPeriodList"]
            )
        }
    else:
        raise DeserializationError("RestrictedPeriods: no recognized variant key")
