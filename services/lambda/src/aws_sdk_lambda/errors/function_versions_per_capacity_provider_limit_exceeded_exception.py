"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersionsPerCapacityProviderLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class FunctionVersionsPerCapacityProviderLimitExceededException_(TypedDict):
    type: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The exception type.</p>"""
    message: NotRequired["aws_sdk_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(
    value: FunctionVersionsPerCapacityProviderLimitExceededException_,
) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(
    data: dict,
) -> FunctionVersionsPerCapacityProviderLimitExceededException_:
    out: FunctionVersionsPerCapacityProviderLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class FunctionVersionsPerCapacityProviderLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#FunctionVersionsPerCapacityProviderLimitExceededException``."""

    code: str | None = "FunctionVersionsPerCapacityProviderLimitExceededException"

    def __init__(
        self, data: FunctionVersionsPerCapacityProviderLimitExceededException_
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FunctionVersionsPerCapacityProviderLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict
    ) -> "FunctionVersionsPerCapacityProviderLimitExceededException":
        return cls(deserialize_json(data))
