"""Generated from Smithy shape ``com.amazonaws.inspector2#AssociateMemberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id


class AssociateMemberResponse(TypedDict, closed=True):
    account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the successfully associated member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateMemberResponse) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> AssociateMemberResponse:
    out: AssociateMemberResponse = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("AssociateMemberResponse.account_id required")
    return out
