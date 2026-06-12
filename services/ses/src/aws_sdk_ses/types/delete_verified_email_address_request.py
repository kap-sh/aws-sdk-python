"""Generated from Smithy shape ``com.amazonaws.ses#DeleteVerifiedEmailAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.address


class DeleteVerifiedEmailAddressRequest(TypedDict):
    email_address: "aws_sdk_ses.types.address.Address"
    """<p>An email address to be removed from the list of verified addresses.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteVerifiedEmailAddressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.EmailAddress", str(value["email_address"])))


def deserialize_query(el: Element) -> DeleteVerifiedEmailAddressRequest:
    out: DeleteVerifiedEmailAddressRequest = {}  # type: ignore[typeddict-item]
    child_email_address = el.find("EmailAddress")
    if child_email_address is not None:
        out["email_address"] = str(child_email_address.text or "")
    else:
        raise DeserializationError(
            "DeleteVerifiedEmailAddressRequest.email_address required"
        )
    return out
