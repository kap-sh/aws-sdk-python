"""Generated from Smithy shape ``com.amazonaws.redshift#RedshiftIdcApplicationAlreadyExistsFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class RedshiftIdcApplicationAlreadyExistsFault_(TypedDict):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RedshiftIdcApplicationAlreadyExistsFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> RedshiftIdcApplicationAlreadyExistsFault_:
    out: RedshiftIdcApplicationAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class RedshiftIdcApplicationAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#RedshiftIdcApplicationAlreadyExistsFault``."""

    code: str | None = "RedshiftIdcApplicationAlreadyExistsFault"

    def __init__(self, data: RedshiftIdcApplicationAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RedshiftIdcApplicationAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "RedshiftIdcApplicationAlreadyExistsFault":
        return cls(deserialize_query(el))
