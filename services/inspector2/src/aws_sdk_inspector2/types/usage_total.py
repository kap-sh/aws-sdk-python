"""Generated from Smithy shape ``com.amazonaws.inspector2#UsageTotal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.metering_account_id
    import aws_sdk_inspector2.types.usage_list


class UsageTotal(TypedDict):
    account_id: NotRequired[
        "aws_sdk_inspector2.types.metering_account_id.MeteringAccountId"
    ]
    """<p>The account ID of the account that usage data was retrieved for.</p>"""
    usage: NotRequired["aws_sdk_inspector2.types.usage_list.UsageList"]
    """<p>An object representing the total usage for an account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageTotal) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "usage" in value:
        import aws_sdk_inspector2.types.usage_list

        out["usage"] = aws_sdk_inspector2.types.usage_list.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> UsageTotal:
    out: UsageTotal = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "usage" in data:
        import aws_sdk_inspector2.types.usage_list

        out["usage"] = aws_sdk_inspector2.types.usage_list.deserialize_json(
            data["usage"]
        )
    return out
