"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceScanNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element
from capo_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudformation.types.error_message


class ResourceScanNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceScanNotFoundException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> ResourceScanNotFoundException_:
    out: ResourceScanNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ResourceScanNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#ResourceScanNotFoundException``."""

    code: str | None = "ResourceScanNotFoundException"

    def __init__(self, data: ResourceScanNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceScanNotFoundException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ResourceScanNotFoundException":
        return cls(deserialize_query(el))
