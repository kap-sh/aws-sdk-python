"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appintegrations.types.application_summary

ApplicationsList: TypeAlias = list[
    "capo_appintegrations.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationsList) -> list:
    import capo_appintegrations.types.application_summary

    out: list = []
    for item in value:
        out.append(capo_appintegrations.types.application_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationsList:
    import capo_appintegrations.types.application_summary

    out: ApplicationsList = []
    for item in data:
        out.append(
            capo_appintegrations.types.application_summary.deserialize_json(item)
        )
    return out
