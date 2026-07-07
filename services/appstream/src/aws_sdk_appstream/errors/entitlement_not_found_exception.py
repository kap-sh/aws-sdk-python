"""Generated from Smithy shape ``com.amazonaws.appstream#EntitlementNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appstream.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appstream.types.error_message


class EntitlementNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appstream.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementNotFoundException_:
    out: EntitlementNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EntitlementNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appstream#EntitlementNotFoundException``."""

    code: str | None = "EntitlementNotFoundException"

    def __init__(self, data: EntitlementNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntitlementNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EntitlementNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
