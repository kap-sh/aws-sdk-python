"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ApplicationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_summary

ApplicationSummaries: TypeAlias = list[
    "capo_service_catalog_appregistry.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummaries) -> list:
    import capo_service_catalog_appregistry.types.application_summary

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog_appregistry.types.application_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApplicationSummaries:
    import capo_service_catalog_appregistry.types.application_summary

    out: ApplicationSummaries = []
    for item in data:
        out.append(
            capo_service_catalog_appregistry.types.application_summary.deserialize_json(
                item
            )
        )
    return out
