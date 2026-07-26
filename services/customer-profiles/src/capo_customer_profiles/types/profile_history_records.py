"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileHistoryRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile_history_record

ProfileHistoryRecords: TypeAlias = list[
    "capo_customer_profiles.types.profile_history_record.ProfileHistoryRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileHistoryRecords) -> list:
    import capo_customer_profiles.types.profile_history_record

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.profile_history_record.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProfileHistoryRecords:
    import capo_customer_profiles.types.profile_history_record

    out: ProfileHistoryRecords = []
    for item in data:
        out.append(
            capo_customer_profiles.types.profile_history_record.deserialize_json(item)
        )
    return out
