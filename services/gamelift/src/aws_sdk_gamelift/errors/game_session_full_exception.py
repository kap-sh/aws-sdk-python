"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionFullException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_gamelift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string


class GameSessionFullException_(TypedDict):
    message: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionFullException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionFullException_:
    out: GameSessionFullException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class GameSessionFullException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gamelift#GameSessionFullException``."""

    code: str | None = "GameSessionFullException"

    def __init__(self, data: GameSessionFullException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GameSessionFullException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "GameSessionFullException":
        return cls(deserialize_aws_json_1_1(data))
