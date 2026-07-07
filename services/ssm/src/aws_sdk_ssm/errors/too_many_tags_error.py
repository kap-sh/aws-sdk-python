"""Generated from Smithy shape ``com.amazonaws.ssm#TooManyTagsError``."""

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import ServiceError


class TooManyTagsError_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyTagsError_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyTagsError_:
    out: TooManyTagsError_ = {}  # type: ignore[typeddict-item]
    return out


class TooManyTagsError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#TooManyTagsError``."""

    code: str | None = "TooManyTagsError"

    def __init__(self, data: TooManyTagsError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TooManyTagsError":
        return cls(deserialize_aws_json_1_1(data))
