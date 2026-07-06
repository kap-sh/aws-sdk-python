"""Generated from Smithy shape ``com.amazonaws.autoscaling#ResourceInUseFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class ResourceInUseFault_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceInUseFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ResourceInUseFault_:
    out: ResourceInUseFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ResourceInUseFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscaling#ResourceInUseFault``."""

    code: str | None = "ResourceInUseFault"

    def __init__(self, data: ResourceInUseFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ResourceInUseFault":
        return cls(deserialize_query(el))
