"""Generated from Smithy shape ``com.amazonaws.autoscaling#LimitExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class LimitExceededFault_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LimitExceededFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> LimitExceededFault_:
    out: LimitExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class LimitExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscaling#LimitExceededFault``."""

    code: str | None = "LimitExceededFault"

    def __init__(self, data: LimitExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "LimitExceededFault":
        return cls(deserialize_query(el))
