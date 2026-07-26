"""Generated from Smithy shape ``com.amazonaws.schemas#ListRegistriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__list_of_registry_summary
    import capo_schemas.types.__string


class ListRegistriesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""
    registries: NotRequired[
        "capo_schemas.types.__list_of_registry_summary.__listOfRegistrySummary"
    ]
    """<p>An array of registry summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistriesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "registries" in value:
        import capo_schemas.types.__list_of_registry_summary

        out["Registries"] = (
            capo_schemas.types.__list_of_registry_summary.serialize_json(
                value["registries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRegistriesResponse:
    out: ListRegistriesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Registries" in data:
        import capo_schemas.types.__list_of_registry_summary

        out["registries"] = (
            capo_schemas.types.__list_of_registry_summary.deserialize_json(
                data["Registries"]
            )
        )
    return out
