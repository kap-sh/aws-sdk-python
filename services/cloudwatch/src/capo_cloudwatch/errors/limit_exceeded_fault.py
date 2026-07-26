"""Generated from Smithy shape ``com.amazonaws.cloudwatch#LimitExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element
from capo_cloudwatch.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch.types.error_message


class LimitExceededFault_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch.types.error_message.ErrorMessage"]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LimitExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LimitExceededFault_:
    out: LimitExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


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
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatch#LimitExceededFault``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "LimitExceededFault":
        return cls(deserialize_aws_json_1_0(data))

    @classmethod
    def from_query(cls, el: Element) -> "LimitExceededFault":
        return cls(deserialize_query(el))
