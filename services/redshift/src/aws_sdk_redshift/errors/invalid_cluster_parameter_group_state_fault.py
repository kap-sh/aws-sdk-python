"""Generated from Smithy shape ``com.amazonaws.redshift#InvalidClusterParameterGroupStateFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class InvalidClusterParameterGroupStateFault_(TypedDict):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidClusterParameterGroupStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidClusterParameterGroupStateFault_:
    out: InvalidClusterParameterGroupStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidClusterParameterGroupStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#InvalidClusterParameterGroupStateFault``."""

    code: str | None = "InvalidClusterParameterGroupStateFault"

    def __init__(self, data: InvalidClusterParameterGroupStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidClusterParameterGroupStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidClusterParameterGroupStateFault":
        return cls(deserialize_query(el))
