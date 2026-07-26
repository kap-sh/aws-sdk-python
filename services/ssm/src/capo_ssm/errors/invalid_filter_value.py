"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidFilterValue_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFilterValue_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFilterValue_:
    out: InvalidFilterValue_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidFilterValue(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidFilterValue``."""

    code: str | None = "InvalidFilterValue"

    def __init__(self, data: InvalidFilterValue_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFilterValue",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidFilterValue":
        return cls(deserialize_aws_json_1_1(data))
