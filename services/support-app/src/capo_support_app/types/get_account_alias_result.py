"""Generated from Smithy shape ``com.amazonaws.supportapp#GetAccountAliasResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support_app.types.aws_account_alias


class GetAccountAliasResult(TypedDict, closed=True):
    account_alias: NotRequired[
        "capo_support_app.types.aws_account_alias.awsAccountAlias"
    ]
    """<p>An alias or short name for an Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountAliasResult) -> dict:
    out: dict = {}
    if "account_alias" in value:
        out["accountAlias"] = value["account_alias"]
    return out


def deserialize_json(data: dict) -> GetAccountAliasResult:
    out: GetAccountAliasResult = {}  # type: ignore[typeddict-item]
    if "accountAlias" in data:
        out["account_alias"] = data["accountAlias"]
    return out
