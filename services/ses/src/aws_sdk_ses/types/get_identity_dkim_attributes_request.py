"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityDkimAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity_list


class GetIdentityDkimAttributesRequest(TypedDict):
    identities: "aws_sdk_ses.types.identity_list.IdentityList"
    """<p>A list of one or more verified identities - email addresses, domains, or both.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityDkimAttributesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.identity_list

    aws_sdk_ses.types.identity_list.serialize_query(
        value["identities"], pairs, f"{prefix}.Identities"
    )


def deserialize_query(el: Element) -> GetIdentityDkimAttributesRequest:
    out: GetIdentityDkimAttributesRequest = {}  # type: ignore[typeddict-item]
    child_identities = el.find("Identities")
    if child_identities is not None:
        import aws_sdk_ses.types.identity_list

        out["identities"] = aws_sdk_ses.types.identity_list.deserialize_query(
            child_identities
        )
    else:
        raise DeserializationError(
            "GetIdentityDkimAttributesRequest.identities required"
        )
    return out
