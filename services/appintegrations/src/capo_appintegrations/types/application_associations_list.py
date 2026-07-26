"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appintegrations.types.application_association_summary

ApplicationAssociationsList: TypeAlias = list[
    "capo_appintegrations.types.application_association_summary.ApplicationAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationAssociationsList) -> list:
    import capo_appintegrations.types.application_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_appintegrations.types.application_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApplicationAssociationsList:
    import capo_appintegrations.types.application_association_summary

    out: ApplicationAssociationsList = []
    for item in data:
        out.append(
            capo_appintegrations.types.application_association_summary.deserialize_json(
                item
            )
        )
    return out
