"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DuplicateResourceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_catalog.types.error_message


class DuplicateResourceException_(TypedDict, closed=True):
    message: NotRequired["capo_service_catalog.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateResourceException_:
    out: DuplicateResourceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DuplicateResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicecatalog#DuplicateResourceException``."""

    code: str | None = "DuplicateResourceException"

    def __init__(self, data: DuplicateResourceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateResourceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DuplicateResourceException":
        return cls(deserialize_aws_json_1_1(data))
