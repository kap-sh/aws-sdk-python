"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message


class ExportNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportNotFoundException_:
    out: ExportNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ExportNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ExportNotFoundException``."""

    code: str | None = "ExportNotFoundException"

    def __init__(self, data: ExportNotFoundException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExportNotFoundException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "ExportNotFoundException":
        return cls(deserialize_aws_json_1_0(data), message)
