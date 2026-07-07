"""Generated from Smithy shape ``com.amazonaws.ses#VerifyDomainDkimRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.domain


class VerifyDomainDkimRequest(TypedDict, closed=True):
    domain: "aws_sdk_ses.types.domain.Domain"
    """<p>The name of the domain to be verified for Easy DKIM signing.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifyDomainDkimRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Domain", str(value["domain"])))


def deserialize_query(el: Element) -> VerifyDomainDkimRequest:
    out: VerifyDomainDkimRequest = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        raise DeserializationError("VerifyDomainDkimRequest.domain required")
    return out
