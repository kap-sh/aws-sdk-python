"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import capo_servicediscovery.types.error_message


class NamespaceNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NamespaceNotFound_:
    out: NamespaceNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NamespaceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#NamespaceNotFound``."""

    code: str | None = "NamespaceNotFound"

    def __init__(self, data: NamespaceNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NamespaceNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NamespaceNotFound":
        return cls(deserialize_aws_json_1_1(data))
