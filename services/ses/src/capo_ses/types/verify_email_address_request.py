"""Generated from Smithy shape ``com.amazonaws.ses#VerifyEmailAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.address


class VerifyEmailAddressRequest(TypedDict, closed=True):
    email_address: "capo_ses.types.address.Address"
    """<p>The email address to be verified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifyEmailAddressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.EmailAddress", str(value["email_address"])))


def deserialize_query(el: Element) -> VerifyEmailAddressRequest:
    out: VerifyEmailAddressRequest = {}  # type: ignore[typeddict-item]
    child_email_address = el.find("EmailAddress")
    if child_email_address is not None:
        out["email_address"] = str(child_email_address.text or "")
    else:
        raise DeserializationError("VerifyEmailAddressRequest.email_address required")
    return out
