"""Generated from Smithy shape ``com.amazonaws.quicksight#OAuthClientApplicationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.o_auth_client_application_summary

OAuthClientApplicationSummaryList: TypeAlias = list[
    "capo_quicksight.types.o_auth_client_application_summary.OAuthClientApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthClientApplicationSummaryList) -> list:
    import capo_quicksight.types.o_auth_client_application_summary

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.o_auth_client_application_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OAuthClientApplicationSummaryList:
    import capo_quicksight.types.o_auth_client_application_summary

    out: OAuthClientApplicationSummaryList = []
    for item in data:
        out.append(
            capo_quicksight.types.o_auth_client_application_summary.deserialize_json(
                item
            )
        )
    return out
