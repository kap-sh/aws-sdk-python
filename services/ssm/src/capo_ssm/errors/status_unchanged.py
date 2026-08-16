"""Generated from Smithy shape ``com.amazonaws.ssm#StatusUnchanged``."""

from typing_extensions import TypedDict

from capo_ssm.errors import ServiceError


class StatusUnchanged_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusUnchanged_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StatusUnchanged_:
    out: StatusUnchanged_ = {}  # type: ignore[typeddict-item]
    return out


class StatusUnchanged(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#StatusUnchanged``."""

    code: str | None = "StatusUnchanged"

    def __init__(self, data: StatusUnchanged_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StatusUnchanged",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "StatusUnchanged":
        return cls(deserialize_aws_json_1_1(data), message)
