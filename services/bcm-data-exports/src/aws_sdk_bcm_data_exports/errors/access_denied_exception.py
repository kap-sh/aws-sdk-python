"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.generic_string


class AccessDeniedException_(TypedDict):
    message: "aws_sdk_bcm_data_exports.types.generic_string.GenericString"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmdataexports#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_1(data))
