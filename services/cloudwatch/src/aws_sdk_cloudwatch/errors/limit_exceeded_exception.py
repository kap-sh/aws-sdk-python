"""Generated from Smithy shape ``com.amazonaws.cloudwatch#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.fault_description


class LimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudwatch.types.fault_description.FaultDescription"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: LimitExceededException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatch#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_0(data))

    @classmethod
    def from_query(cls, el: Element) -> "LimitExceededException":
        return cls(deserialize_query(el))
