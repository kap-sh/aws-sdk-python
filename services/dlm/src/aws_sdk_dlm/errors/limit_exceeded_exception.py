"""Generated from Smithy shape ``com.amazonaws.dlm#LimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dlm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dlm.types.error_code
    import aws_sdk_dlm.types.error_message
    import aws_sdk_dlm.types.string


class LimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_dlm.types.error_message.ErrorMessage"]
    code: NotRequired["aws_sdk_dlm.types.error_code.ErrorCode"]
    resource_type: NotRequired["aws_sdk_dlm.types.string.String"]
    """<p>Value is the type of resource for which a limit was exceeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dlm#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_json(data))
