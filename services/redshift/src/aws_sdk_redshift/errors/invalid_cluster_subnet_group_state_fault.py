"""Generated from Smithy shape ``com.amazonaws.redshift#InvalidClusterSubnetGroupStateFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class InvalidClusterSubnetGroupStateFault_(TypedDict):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidClusterSubnetGroupStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidClusterSubnetGroupStateFault_:
    out: InvalidClusterSubnetGroupStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidClusterSubnetGroupStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#InvalidClusterSubnetGroupStateFault``."""

    code: str | None = "InvalidClusterSubnetGroupStateFault"

    def __init__(self, data: InvalidClusterSubnetGroupStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidClusterSubnetGroupStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidClusterSubnetGroupStateFault":
        return cls(deserialize_query(el))
