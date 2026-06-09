"""Generated from Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyConfigNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class ProvisionedConcurrencyConfigNotFoundException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedConcurrencyConfigNotFoundException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ProvisionedConcurrencyConfigNotFoundException_:
    out: ProvisionedConcurrencyConfigNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ProvisionedConcurrencyConfigNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyConfigNotFoundException``."""

    code: str | None = "ProvisionedConcurrencyConfigNotFoundException"

    def __init__(self, data: ProvisionedConcurrencyConfigNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ProvisionedConcurrencyConfigNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ProvisionedConcurrencyConfigNotFoundException":
        return cls(deserialize_json(data))
