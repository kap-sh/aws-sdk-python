"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotCopyAlreadyEnabledFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class SnapshotCopyAlreadyEnabledFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotCopyAlreadyEnabledFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> SnapshotCopyAlreadyEnabledFault_:
    out: SnapshotCopyAlreadyEnabledFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SnapshotCopyAlreadyEnabledFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#SnapshotCopyAlreadyEnabledFault``."""

    code: str | None = "SnapshotCopyAlreadyEnabledFault"

    def __init__(self, data: SnapshotCopyAlreadyEnabledFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapshotCopyAlreadyEnabledFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "SnapshotCopyAlreadyEnabledFault":
        return cls(deserialize_query(el))
