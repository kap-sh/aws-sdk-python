"""Generated from Smithy shape ``com.amazonaws.neptune#InvalidVPCNetworkStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element
from aws_sdk_neptune.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune.types.exception_message


class InvalidVPCNetworkStateFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_neptune.types.exception_message.ExceptionMessage"]
    """<p>A message describing the details of the problem.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidVPCNetworkStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidVPCNetworkStateFault_:
    out: InvalidVPCNetworkStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidVPCNetworkStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptune#InvalidVPCNetworkStateFault``."""

    code: str | None = "InvalidVPCNetworkStateFault"

    def __init__(self, data: InvalidVPCNetworkStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidVPCNetworkStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidVPCNetworkStateFault":
        return cls(deserialize_query(el))
