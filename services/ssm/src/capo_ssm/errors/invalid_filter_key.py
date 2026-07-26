"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidFilterKey``."""

from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvalidFilterKey_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFilterKey_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFilterKey_:
    out: InvalidFilterKey_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidFilterKey(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidFilterKey``."""

    code: str | None = "InvalidFilterKey"

    def __init__(self, data: InvalidFilterKey_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFilterKey",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidFilterKey":
        return cls(deserialize_aws_json_1_1(data))
