"""Generated from Smithy shape ``com.amazonaws.appstream#EntitlementAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appstream.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appstream.types.error_message


class EntitlementAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_appstream.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementAlreadyExistsException_:
    out: EntitlementAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EntitlementAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appstream#EntitlementAlreadyExistsException``."""

    code: str | None = "EntitlementAlreadyExistsException"

    def __init__(self, data: EntitlementAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntitlementAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EntitlementAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
