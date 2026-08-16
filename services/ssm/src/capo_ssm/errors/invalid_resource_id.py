"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidResourceId``."""

from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class InvalidResourceId_(TypedDict, closed=True):
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

    def __init__(self, data: InvalidResourceId_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceId",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "InvalidResourceId":
        return cls(deserialize_aws_json_1_1(data), message)
