"""Generated from Smithy shape ``com.amazonaws.ses#ListIdentitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity_list
    import aws_sdk_ses.types.next_token


class ListIdentitiesResponse(TypedDict):
    identities: "aws_sdk_ses.types.identity_list.IdentityList"
    """<p>A list of identities.</p>"""
    next_token: NotRequired["aws_sdk_ses.types.next_token.NextToken"]
    """<p>The token used for pagination.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListIdentitiesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.identity_list

    aws_sdk_ses.types.identity_list.serialize_query(
        value["identities"], pairs, f"{prefix}.Identities"
    )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListIdentitiesResponse:
    out: ListIdentitiesResponse = {}  # type: ignore[typeddict-item]
    child_identities = el.find("Identities")
    if child_identities is not None:
        import aws_sdk_ses.types.identity_list

        out["identities"] = aws_sdk_ses.types.identity_list.deserialize_query(
            child_identities
        )
    else:
        raise DeserializationError("ListIdentitiesResponse.identities required")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
