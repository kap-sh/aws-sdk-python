"""Generated from Smithy shape ``com.amazonaws.codecatalyst#AccessTokenSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.access_token_summary

AccessTokenSummaries: TypeAlias = list[
    "capo_codecatalyst.types.access_token_summary.AccessTokenSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessTokenSummaries) -> list:
    import capo_codecatalyst.types.access_token_summary

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.access_token_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessTokenSummaries:
    import capo_codecatalyst.types.access_token_summary

    out: AccessTokenSummaries = []
    for item in data:
        out.append(capo_codecatalyst.types.access_token_summary.deserialize_json(item))
    return out
