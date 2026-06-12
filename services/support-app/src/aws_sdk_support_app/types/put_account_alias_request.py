"""Generated from Smithy shape ``com.amazonaws.supportapp#PutAccountAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support_app.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support_app.types.aws_account_alias


class PutAccountAliasRequest(TypedDict):
    account_alias: "aws_sdk_support_app.types.aws_account_alias.awsAccountAlias"
    """<p>An alias or short name for an Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountAliasRequest) -> dict:
    out: dict = {}
    out["accountAlias"] = value["account_alias"]
    return out


def deserialize_json(data: dict) -> PutAccountAliasRequest:
    out: PutAccountAliasRequest = {}  # type: ignore[typeddict-item]
    if "accountAlias" in data:
        out["account_alias"] = data["accountAlias"]
    else:
        raise DeserializationError("PutAccountAliasRequest.account_alias required")
    return out
