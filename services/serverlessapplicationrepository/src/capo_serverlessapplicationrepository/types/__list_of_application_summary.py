"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfApplicationSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.application_summary

__listOfApplicationSummary: TypeAlias = list[
    "capo_serverlessapplicationrepository.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfApplicationSummary) -> list:
    import capo_serverlessapplicationrepository.types.application_summary

    out: list = []
    for item in value:
        out.append(
            capo_serverlessapplicationrepository.types.application_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfApplicationSummary:
    import capo_serverlessapplicationrepository.types.application_summary

    out: __listOfApplicationSummary = []
    for item in data:
        out.append(
            capo_serverlessapplicationrepository.types.application_summary.deserialize_json(
                item
            )
        )
    return out
