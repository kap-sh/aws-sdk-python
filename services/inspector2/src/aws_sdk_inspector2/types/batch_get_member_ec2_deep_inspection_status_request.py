"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetMemberEc2DeepInspectionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id_set


class BatchGetMemberEc2DeepInspectionStatusRequest(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_inspector2.types.account_id_set.AccountIdSet"]
    """<p>The unique identifiers for the Amazon Web Services accounts to retrieve Amazon Inspector deep inspection activation status for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMemberEc2DeepInspectionStatusRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_inspector2.types.account_id_set

        out["accountIds"] = aws_sdk_inspector2.types.account_id_set.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetMemberEc2DeepInspectionStatusRequest:
    out: BatchGetMemberEc2DeepInspectionStatusRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.account_id_set

        out["account_ids"] = aws_sdk_inspector2.types.account_id_set.deserialize_json(
            data["accountIds"]
        )
    return out
