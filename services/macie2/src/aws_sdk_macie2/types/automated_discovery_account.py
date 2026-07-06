"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.automated_discovery_account_status


class AutomatedDiscoveryAccount(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account.</p>"""
    status: NotRequired[
        "aws_sdk_macie2.types.automated_discovery_account_status.AutomatedDiscoveryAccountStatus"
    ]
    """<p>The current status of automated sensitive data discovery for the account. Possible values are: ENABLED, perform automated sensitive data discovery activities for the account; and, DISABLED, don't perform automated sensitive data discovery activities for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedDiscoveryAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import aws_sdk_macie2.types.automated_discovery_account_status

        out["status"] = (
            aws_sdk_macie2.types.automated_discovery_account_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedDiscoveryAccount:
    out: AutomatedDiscoveryAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "status" in data:
        import aws_sdk_macie2.types.automated_discovery_account_status

        out["status"] = (
            aws_sdk_macie2.types.automated_discovery_account_status.deserialize_json(
                data["status"]
            )
        )
    return out
