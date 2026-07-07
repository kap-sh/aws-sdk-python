"""Generated from Smithy shape ``com.amazonaws.health#InvalidPaginationToken``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_health.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_health.types.string


class InvalidPaginationToken_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_health.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPaginationToken_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPaginationToken_:
    out: InvalidPaginationToken_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidPaginationToken(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.health#InvalidPaginationToken``."""

    code: str | None = "InvalidPaginationToken"

    def __init__(self, data: InvalidPaginationToken_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationToken",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPaginationToken":
        return cls(deserialize_aws_json_1_1(data))
