"""Generated from Smithy shape ``com.amazonaws.redshift#InvalidClusterSnapshotScheduleStateFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class InvalidClusterSnapshotScheduleStateFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidClusterSnapshotScheduleStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidClusterSnapshotScheduleStateFault_:
    out: InvalidClusterSnapshotScheduleStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidClusterSnapshotScheduleStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#InvalidClusterSnapshotScheduleStateFault``."""

    code: str | None = "InvalidClusterSnapshotScheduleStateFault"

    def __init__(self, data: InvalidClusterSnapshotScheduleStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidClusterSnapshotScheduleStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidClusterSnapshotScheduleStateFault":
        return cls(deserialize_query(el))
