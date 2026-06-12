"""Generated from Smithy shape ``com.amazonaws.inspector2#Account``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_inspector2.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.resource_status
    import aws_sdk_inspector2.types.status

class Account(TypedDict):
    account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account.</p>"""
    status: "aws_sdk_inspector2.types.status.Status"
    """<p>The status of Amazon Inspector for the account.</p>"""
    resource_status: "aws_sdk_inspector2.types.resource_status.ResourceStatus"
    """<p>Details of the status of Amazon Inspector scans by resource type.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["status"] = value["status"]
    import aws_sdk_inspector2.types.resource_status
    out["resourceStatus"] = aws_sdk_inspector2.types.resource_status.serialize_json(value["resource_status"])
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("Account.account_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("Account.status required")
    if "resourceStatus" in data:
        import aws_sdk_inspector2.types.resource_status
        out["resource_status"] = aws_sdk_inspector2.types.resource_status.deserialize_json(data["resourceStatus"])
    else:
        raise DeserializationError("Account.resource_status required")
    return out