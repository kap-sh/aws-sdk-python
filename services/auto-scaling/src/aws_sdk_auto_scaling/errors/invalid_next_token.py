"""Generated from Smithy shape ``com.amazonaws.autoscaling#InvalidNextToken``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class InvalidNextToken_(TypedDict):
    message: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidNextToken_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidNextToken_:
    out: InvalidNextToken_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidNextToken(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscaling#InvalidNextToken``."""

    code: str | None = "InvalidNextToken"

    def __init__(self, data: InvalidNextToken_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextToken",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidNextToken":
        return cls(deserialize_query(el))
