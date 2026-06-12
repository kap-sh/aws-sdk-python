"""Generated from Smithy shape ``com.amazonaws.gamelift#TerminalRoutingStrategyException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string


class TerminalRoutingStrategyException_(TypedDict):
    message: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminalRoutingStrategyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminalRoutingStrategyException_:
    out: TerminalRoutingStrategyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TerminalRoutingStrategyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#TerminalRoutingStrategyException``."""

    code: str | None = "TerminalRoutingStrategyException"

    def __init__(self, data: TerminalRoutingStrategyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TerminalRoutingStrategyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TerminalRoutingStrategyException":
        return cls(deserialize_aws_json_1_1(data))
