"""Generated from Smithy shape ``com.amazonaws.connect#AuthenticationProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.authentication_profile_summary

AuthenticationProfileSummaryList: TypeAlias = list[
    "capo_connect.types.authentication_profile_summary.AuthenticationProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationProfileSummaryList) -> list:
    import capo_connect.types.authentication_profile_summary

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.authentication_profile_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuthenticationProfileSummaryList:
    import capo_connect.types.authentication_profile_summary

    out: AuthenticationProfileSummaryList = []
    for item in data:
        out.append(
            capo_connect.types.authentication_profile_summary.deserialize_json(item)
        )
    return out
