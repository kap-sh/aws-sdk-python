"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidCommandId``."""

from typing import TypedDict

from aws_sdk_ssm.errors import ServiceError


class InvalidCommandId_(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidCommandId_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidCommandId_:
    out: InvalidCommandId_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidCommandId(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidCommandId``."""

    code: str | None = "InvalidCommandId"

    def __init__(self, data: InvalidCommandId_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCommandId",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidCommandId":
        return cls(deserialize_aws_json_1_1(data))
