"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PoolOriginationIdentitiesFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter

PoolOriginationIdentitiesFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter.PoolOriginationIdentitiesFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PoolOriginationIdentitiesFilterList) -> list:
    import capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PoolOriginationIdentitiesFilterList:
    import capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter

    out: PoolOriginationIdentitiesFilterList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.pool_origination_identities_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
