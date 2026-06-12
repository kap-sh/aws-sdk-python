"""Generated from Smithy shape ``com.amazonaws.guardduty#RemoteAccountDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.string


class RemoteAccountDetails(TypedDict):
    account_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID of the remote API caller.</p>"""
    affiliated: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Details on whether the Amazon Web Services account of the remote API caller is related to your GuardDuty environment. If this value is <code>True</code> the API caller is affiliated to your account in some way. If it is <code>False</code> the API caller is from outside your environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAccountDetails) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "affiliated" in value:
        out["affiliated"] = value["affiliated"]
    return out


def deserialize_json(data: dict) -> RemoteAccountDetails:
    out: RemoteAccountDetails = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "affiliated" in data:
        out["affiliated"] = data["affiliated"]
    return out
