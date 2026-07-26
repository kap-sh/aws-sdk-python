"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationNotSupportedException``."""

from typing_extensions import TypedDict

from capo_workspaces.errors import ServiceError


class ApplicationNotSupportedException_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationNotSupportedException_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationNotSupportedException_:
    out: ApplicationNotSupportedException_ = {}  # type: ignore[typeddict-item]
    return out


class ApplicationNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#ApplicationNotSupportedException``."""

    code: str | None = "ApplicationNotSupportedException"

    def __init__(self, data: ApplicationNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ApplicationNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ApplicationNotSupportedException":
        return cls(deserialize_aws_json_1_1(data))
