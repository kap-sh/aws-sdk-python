"""Generated from Smithy shape ``com.amazonaws.inspector2#GetMemberRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id


class GetMemberRequest(TypedDict):
    account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member account to retrieve information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemberRequest) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> GetMemberRequest:
    out: GetMemberRequest = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("GetMemberRequest.account_id required")
    return out
