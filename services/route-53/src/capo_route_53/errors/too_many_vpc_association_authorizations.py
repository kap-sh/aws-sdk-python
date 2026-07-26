"""Generated from Smithy shape ``com.amazonaws.route53#TooManyVPCAssociationAuthorizations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53.types.error_message


class TooManyVPCAssociationAuthorizations_(TypedDict, closed=True):
    message: NotRequired["capo_route_53.types.error_message.ErrorMessage"]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyVPCAssociationAuthorizations_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyVPCAssociationAuthorizations_:
    out: TooManyVPCAssociationAuthorizations_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyVPCAssociationAuthorizations(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#TooManyVPCAssociationAuthorizations``."""

    code: str | None = "TooManyVPCAssociationAuthorizations"

    def __init__(self, data: TooManyVPCAssociationAuthorizations_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyVPCAssociationAuthorizations",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "TooManyVPCAssociationAuthorizations":
        return cls(deserialize_xml(el))
