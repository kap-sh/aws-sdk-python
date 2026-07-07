"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.generic_string


class InternalServerException_(TypedDict, closed=True):
    message: "aws_sdk_bcm_data_exports.types.generic_string.GenericString"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmdataexports#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data))
