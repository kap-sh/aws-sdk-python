"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfilesSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.security_profile_search_summary

SecurityProfilesSearchSummaryList: TypeAlias = list[
    "capo_connect.types.security_profile_search_summary.SecurityProfileSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfilesSearchSummaryList) -> list:
    import capo_connect.types.security_profile_search_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.security_profile_search_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityProfilesSearchSummaryList:
    import capo_connect.types.security_profile_search_summary

    out: SecurityProfilesSearchSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.security_profile_search_summary.deserialize_json(item)
        )
    return out
