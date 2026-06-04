"""Generated from Smithy shape ``com.amazonaws.iam#DeleteAccountAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.account_alias_type


class DeleteAccountAliasRequest(TypedDict):
    account_alias: "aws_sdk_iam.types.account_alias_type.accountAliasType"
    """<p>The name of the account alias to delete.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAccountAliasRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.AccountAlias", str(value["account_alias"])))


def deserialize_query(el: Element) -> DeleteAccountAliasRequest:
    out: DeleteAccountAliasRequest = {}  # type: ignore[typeddict-item]
    child_account_alias = el.find("AccountAlias")
    if child_account_alias is not None:
        out["account_alias"] = str(child_account_alias.text or "")
    else:
        raise DeserializationError("DeleteAccountAliasRequest.account_alias required")
    return out
