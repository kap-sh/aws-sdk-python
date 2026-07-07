"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryMemberOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.account_id


class ProtectedQueryMemberOutputConfiguration(TypedDict, closed=True):
    account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The unique identifier for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryMemberOutputConfiguration) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedQueryMemberOutputConfiguration:
    out: ProtectedQueryMemberOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "ProtectedQueryMemberOutputConfiguration.account_id required"
        )
    return out
