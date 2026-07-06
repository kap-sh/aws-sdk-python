"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityVerificationAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity_list


class GetIdentityVerificationAttributesRequest(TypedDict, closed=True):
    identities: "aws_sdk_ses.types.identity_list.IdentityList"
    """<p>A list of identities.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityVerificationAttributesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_ses.types.identity_list

    aws_sdk_ses.types.identity_list.serialize_query(
        value["identities"], pairs, f"{prefix}.Identities"
    )


def deserialize_query(el: Element) -> GetIdentityVerificationAttributesRequest:
    out: GetIdentityVerificationAttributesRequest = {}  # type: ignore[typeddict-item]
    child_identities = el.find("Identities")
    if child_identities is not None:
        import aws_sdk_ses.types.identity_list

        out["identities"] = aws_sdk_ses.types.identity_list.deserialize_query(
            child_identities
        )
    else:
        raise DeserializationError(
            "GetIdentityVerificationAttributesRequest.identities required"
        )
    return out
