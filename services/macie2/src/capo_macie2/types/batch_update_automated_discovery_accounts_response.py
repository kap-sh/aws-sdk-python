"""Generated from Smithy shape ``com.amazonaws.macie2#BatchUpdateAutomatedDiscoveryAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_automated_discovery_account_update_error


class BatchUpdateAutomatedDiscoveryAccountsResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_macie2.types.__list_of_automated_discovery_account_update_error.__listOfAutomatedDiscoveryAccountUpdateError"
    ]
    """<p>An array of objects, one for each account whose status wasn't changed. Each object identifies the account and explains why the status of automated sensitive data discovery wasn't changed for the account. This value is null if the request succeeded for all specified accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateAutomatedDiscoveryAccountsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_macie2.types.__list_of_automated_discovery_account_update_error

        out["errors"] = (
            capo_macie2.types.__list_of_automated_discovery_account_update_error.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateAutomatedDiscoveryAccountsResponse:
    out: BatchUpdateAutomatedDiscoveryAccountsResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_macie2.types.__list_of_automated_discovery_account_update_error

        out["errors"] = (
            capo_macie2.types.__list_of_automated_discovery_account_update_error.deserialize_json(
                data["errors"]
            )
        )
    return out
