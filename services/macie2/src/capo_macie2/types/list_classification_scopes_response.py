"""Generated from Smithy shape ``com.amazonaws.macie2#ListClassificationScopesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_classification_scope_summary
    import capo_macie2.types.next_token


class ListClassificationScopesResponse(TypedDict, closed=True):
    classification_scopes: NotRequired[
        "capo_macie2.types.__list_of_classification_scope_summary.__listOfClassificationScopeSummary"
    ]
    """<p>An array that specifies the unique identifier and name of the classification scope for the account.</p>"""
    next_token: NotRequired["capo_macie2.types.next_token.NextToken"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClassificationScopesResponse) -> dict:
    out: dict = {}
    if "classification_scopes" in value:
        import capo_macie2.types.__list_of_classification_scope_summary

        out["classificationScopes"] = (
            capo_macie2.types.__list_of_classification_scope_summary.serialize_json(
                value["classification_scopes"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClassificationScopesResponse:
    out: ListClassificationScopesResponse = {}  # type: ignore[typeddict-item]
    if "classificationScopes" in data:
        import capo_macie2.types.__list_of_classification_scope_summary

        out["classification_scopes"] = (
            capo_macie2.types.__list_of_classification_scope_summary.deserialize_json(
                data["classificationScopes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
