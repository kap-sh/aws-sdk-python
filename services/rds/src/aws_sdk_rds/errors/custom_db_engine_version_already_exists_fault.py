"""Generated from Smithy shape ``com.amazonaws.rds#CustomDBEngineVersionAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class CustomDBEngineVersionAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomDBEngineVersionAlreadyExistsFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CustomDBEngineVersionAlreadyExistsFault_:
    out: CustomDBEngineVersionAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CustomDBEngineVersionAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#CustomDBEngineVersionAlreadyExistsFault``."""

    code: str | None = "CustomDBEngineVersionAlreadyExistsFault"

    def __init__(self, data: CustomDBEngineVersionAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomDBEngineVersionAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CustomDBEngineVersionAlreadyExistsFault":
        return cls(deserialize_query(el))
