"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#ForbiddenException``."""

from typing_extensions import TypedDict

from aws_sdk_apigatewaymanagementapi.errors import ServiceError


class ForbiddenException_(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenException_) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apigatewaymanagementapi#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(self, data: ForbiddenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ForbiddenException":
        return cls(deserialize_json(data))
