"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobSingleMemberOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id


class ProtectedJobSingleMemberOutput(TypedDict):
    account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member in the collaboration who can receive results from analyses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobSingleMemberOutput) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedJobSingleMemberOutput:
    out: ProtectedJobSingleMemberOutput = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("ProtectedJobSingleMemberOutput.account_id required")
    return out
