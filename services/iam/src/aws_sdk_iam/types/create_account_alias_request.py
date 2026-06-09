"""Generated from Smithy shape ``com.amazonaws.iam#CreateAccountAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.account_alias_type


class CreateAccountAliasRequest(TypedDict):
    account_alias: "aws_sdk_iam.types.account_alias_type.accountAliasType"
    """<p>The account alias to create.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateAccountAliasRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.AccountAlias", str(value["account_alias"])))


def deserialize_query(el: Element) -> CreateAccountAliasRequest:
    out: CreateAccountAliasRequest = {}  # type: ignore[typeddict-item]
    child_account_alias = el.find("AccountAlias")
    if child_account_alias is not None:
        out["account_alias"] = str(child_account_alias.text or "")
    else:
        raise DeserializationError("CreateAccountAliasRequest.account_alias required")
    return out
