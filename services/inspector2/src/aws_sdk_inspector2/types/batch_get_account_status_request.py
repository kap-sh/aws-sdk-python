"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetAccountStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id_set


class BatchGetAccountStatusRequest(TypedDict):
    account_ids: NotRequired["aws_sdk_inspector2.types.account_id_set.AccountIdSet"]
    """<p>The 12-digit Amazon Web Services account IDs of the accounts to retrieve Amazon Inspector status for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAccountStatusRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_inspector2.types.account_id_set

        out["accountIds"] = aws_sdk_inspector2.types.account_id_set.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetAccountStatusRequest:
    out: BatchGetAccountStatusRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.account_id_set

        out["account_ids"] = aws_sdk_inspector2.types.account_id_set.deserialize_json(
            data["accountIds"]
        )
    return out
