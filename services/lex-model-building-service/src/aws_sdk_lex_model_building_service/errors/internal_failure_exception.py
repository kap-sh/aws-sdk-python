"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#InternalFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_model_building_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.string


class InternalFailureException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalFailureException_:
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexmodelbuildingservice#InternalFailureException``."""

    code: str | None = "InternalFailureException"

    def __init__(self, data: InternalFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalFailureException":
        return cls(deserialize_json(data))
