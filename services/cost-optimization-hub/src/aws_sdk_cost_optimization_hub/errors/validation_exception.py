"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_optimization_hub.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.validation_exception_details
    import aws_sdk_cost_optimization_hub.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "str"
    reason: NotRequired[
        "aws_sdk_cost_optimization_hub.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the validation exception.</p>"""
    fields: NotRequired[
        "aws_sdk_cost_optimization_hub.types.validation_exception_details.ValidationExceptionDetails"
    ]
    """<p>The list of fields that are invalid.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import aws_sdk_cost_optimization_hub.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_cost_optimization_hub.types.validation_exception_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    if "fields" in value:
        import aws_sdk_cost_optimization_hub.types.validation_exception_details

        out["fields"] = (
            aws_sdk_cost_optimization_hub.types.validation_exception_details.serialize_aws_json_1_0(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "reason" in data:
        import aws_sdk_cost_optimization_hub.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_cost_optimization_hub.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    if "fields" in data:
        import aws_sdk_cost_optimization_hub.types.validation_exception_details

        out["fields"] = (
            aws_sdk_cost_optimization_hub.types.validation_exception_details.deserialize_aws_json_1_0(
                data["fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costoptimizationhub#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ValidationException":
        return cls(deserialize_aws_json_1_0(data))
