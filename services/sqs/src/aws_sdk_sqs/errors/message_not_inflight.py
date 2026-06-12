"""Generated from Smithy shape ``com.amazonaws.sqs#MessageNotInflight``."""

from typing import TypedDict

from aws_sdk_sqs.errors import ServiceError


class MessageNotInflight_(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageNotInflight_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageNotInflight_:
    out: MessageNotInflight_ = {}  # type: ignore[typeddict-item]
    return out


class MessageNotInflight(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sqs#MessageNotInflight``."""

    code: str | None = "MessageNotInflight"

    def __init__(self, data: MessageNotInflight_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MessageNotInflight",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "MessageNotInflight":
        return cls(deserialize_aws_json_1_0(data))
