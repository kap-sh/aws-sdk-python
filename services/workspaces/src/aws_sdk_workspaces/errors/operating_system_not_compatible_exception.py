"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemNotCompatibleException``."""

from typing import TypedDict

from aws_sdk_workspaces.errors import ServiceError


class OperatingSystemNotCompatibleException_(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemNotCompatibleException_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> OperatingSystemNotCompatibleException_:
    out: OperatingSystemNotCompatibleException_ = {}  # type: ignore[typeddict-item]
    return out


class OperatingSystemNotCompatibleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#OperatingSystemNotCompatibleException``."""

    code: str | None = "OperatingSystemNotCompatibleException"

    def __init__(self, data: OperatingSystemNotCompatibleException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperatingSystemNotCompatibleException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OperatingSystemNotCompatibleException":
        return cls(deserialize_aws_json_1_1(data))
