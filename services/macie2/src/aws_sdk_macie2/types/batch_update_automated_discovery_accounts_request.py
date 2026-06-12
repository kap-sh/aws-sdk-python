"""Generated from Smithy shape ``com.amazonaws.macie2#BatchUpdateAutomatedDiscoveryAccountsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_automated_discovery_account_update


class BatchUpdateAutomatedDiscoveryAccountsRequest(TypedDict):
    accounts: NotRequired[
        "aws_sdk_macie2.types.__list_of_automated_discovery_account_update.__listOfAutomatedDiscoveryAccountUpdate"
    ]
    """<p>An array of objects, one for each account to change the status of automated sensitive data discovery for. Each object specifies the Amazon Web Services account ID for an account and a new status for that account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateAutomatedDiscoveryAccountsRequest) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_macie2.types.__list_of_automated_discovery_account_update

        out["accounts"] = (
            aws_sdk_macie2.types.__list_of_automated_discovery_account_update.serialize_json(
                value["accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateAutomatedDiscoveryAccountsRequest:
    out: BatchUpdateAutomatedDiscoveryAccountsRequest = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import aws_sdk_macie2.types.__list_of_automated_discovery_account_update

        out["accounts"] = (
            aws_sdk_macie2.types.__list_of_automated_discovery_account_update.deserialize_json(
                data["accounts"]
            )
        )
    return out
