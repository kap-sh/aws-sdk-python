"""Generated from Smithy shape ``com.amazonaws.snowball#UnsupportedAddressException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import ServiceError

if TYPE_CHECKING:
    import capo_snowball.types.string


class UnsupportedAddressException_(TypedDict, closed=True):
    message: NotRequired["capo_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedAddressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedAddressException_:
    out: UnsupportedAddressException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedAddressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#UnsupportedAddressException``."""

    code: str | None = "UnsupportedAddressException"

    def __init__(self, data: UnsupportedAddressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedAddressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedAddressException":
        return cls(deserialize_aws_json_1_1(data))
