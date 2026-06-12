"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFInvalidParameterException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.error_message
    import aws_sdk_wafv2.types.error_reason
    import aws_sdk_wafv2.types.parameter_exception_field
    import aws_sdk_wafv2.types.parameter_exception_parameter


class WAFInvalidParameterException_(TypedDict):
    message: NotRequired["aws_sdk_wafv2.types.error_message.ErrorMessage"]
    field: NotRequired[
        "aws_sdk_wafv2.types.parameter_exception_field.ParameterExceptionField"
    ]
    """<p>The settings where the invalid parameter was found. </p>"""
    parameter: NotRequired[
        "aws_sdk_wafv2.types.parameter_exception_parameter.ParameterExceptionParameter"
    ]
    """<p>The invalid parameter that resulted in the exception. </p>"""
    reason: NotRequired["aws_sdk_wafv2.types.error_reason.ErrorReason"]
    """<p>Additional information about the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInvalidParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "field" in value:
        import aws_sdk_wafv2.types.parameter_exception_field

        out["Field"] = (
            aws_sdk_wafv2.types.parameter_exception_field.serialize_aws_json_1_1(
                value["field"]
            )
        )
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInvalidParameterException_:
    out: WAFInvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "Field" in data:
        import aws_sdk_wafv2.types.parameter_exception_field

        out["field"] = (
            aws_sdk_wafv2.types.parameter_exception_field.deserialize_aws_json_1_1(
                data["Field"]
            )
        )
    if "Parameter" in data:
        out["parameter"] = data["Parameter"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out


class WAFInvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFInvalidParameterException``."""

    code: str | None = "WAFInvalidParameterException"

    def __init__(self, data: WAFInvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFInvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFInvalidParameterException":
        return cls(deserialize_aws_json_1_1(data))
