"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidResourceId``."""

from typing import TypedDict

from aws_sdk_ssm.errors import ServiceError


class InvalidResourceId_(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidResourceId_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidResourceId_:
    out: InvalidResourceId_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidResourceId(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidResourceId``."""

    code: str | None = "InvalidResourceId"

    def __init__(self, data: InvalidResourceId_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceId",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidResourceId":
        return cls(deserialize_aws_json_1_1(data))
