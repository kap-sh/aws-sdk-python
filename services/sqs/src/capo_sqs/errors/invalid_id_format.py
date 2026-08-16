"""Generated from Smithy shape ``com.amazonaws.sqs#InvalidIdFormat``."""

from typing_extensions import TypedDict

from capo_sqs.errors import ServiceError


class InvalidIdFormat_(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidIdFormat_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidIdFormat_:
    out: InvalidIdFormat_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidIdFormat(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#InvalidIdFormat``."""

    code: str | None = "InvalidIdFormat"

    def __init__(self, data: InvalidIdFormat_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidIdFormat",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "InvalidIdFormat":
        return cls(deserialize_aws_json_1_0(data), message)
