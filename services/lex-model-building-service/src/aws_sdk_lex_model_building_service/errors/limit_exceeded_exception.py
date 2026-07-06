"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_model_building_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.string


class LimitExceededException_(TypedDict, closed=True):
    retry_after_seconds: NotRequired[
        "aws_sdk_lex_model_building_service.types.string.String"
    ]
    message: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexmodelbuildingservice#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_json(data))
