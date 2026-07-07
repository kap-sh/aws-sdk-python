"""Generated from Smithy shape ``com.amazonaws.autoscaling#IrreversibleInstanceRefreshFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class IrreversibleInstanceRefreshFault_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: IrreversibleInstanceRefreshFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> IrreversibleInstanceRefreshFault_:
    out: IrreversibleInstanceRefreshFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class IrreversibleInstanceRefreshFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscaling#IrreversibleInstanceRefreshFault``."""

    code: str | None = "IrreversibleInstanceRefreshFault"

    def __init__(self, data: IrreversibleInstanceRefreshFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IrreversibleInstanceRefreshFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "IrreversibleInstanceRefreshFault":
        return cls(deserialize_query(el))
