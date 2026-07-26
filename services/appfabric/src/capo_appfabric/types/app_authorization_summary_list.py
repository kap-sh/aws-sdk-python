"""Generated from Smithy shape ``com.amazonaws.appfabric#AppAuthorizationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appfabric.types.app_authorization_summary

AppAuthorizationSummaryList: TypeAlias = list[
    "capo_appfabric.types.app_authorization_summary.AppAuthorizationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppAuthorizationSummaryList) -> list:
    import capo_appfabric.types.app_authorization_summary

    out: list = []
    for item in value:
        out.append(capo_appfabric.types.app_authorization_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppAuthorizationSummaryList:
    import capo_appfabric.types.app_authorization_summary

    out: AppAuthorizationSummaryList = []
    for item in data:
        out.append(
            capo_appfabric.types.app_authorization_summary.deserialize_json(item)
        )
    return out
