"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidNextToken``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidNextToken_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidNextToken_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidNextToken_:
    out: InvalidNextToken_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidNextToken(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidNextToken``."""

    code: str | None = "InvalidNextToken"

    def __init__(self, data: InvalidNextToken_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextToken",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidNextToken":
        return cls(deserialize_aws_json_1_1(data))
