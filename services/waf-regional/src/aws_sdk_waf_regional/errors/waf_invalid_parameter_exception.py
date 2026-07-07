"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFInvalidParameterException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.parameter_exception_field
    import aws_sdk_waf_regional.types.parameter_exception_parameter
    import aws_sdk_waf_regional.types.parameter_exception_reason


class WAFInvalidParameterException_(TypedDict, closed=True):
    field: NotRequired[
        "aws_sdk_waf_regional.types.parameter_exception_field.ParameterExceptionField"
    ]
    parameter: NotRequired[
        "aws_sdk_waf_regional.types.parameter_exception_parameter.ParameterExceptionParameter"
    ]
    reason: NotRequired[
        "aws_sdk_waf_regional.types.parameter_exception_reason.ParameterExceptionReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInvalidParameterException_) -> dict:
    out: dict = {}
    if "field" in value:
        import aws_sdk_waf_regional.types.parameter_exception_field

        out["field"] = (
            aws_sdk_waf_regional.types.parameter_exception_field.serialize_aws_json_1_1(
                value["field"]
            )
        )
    if "parameter" in value:
        out["parameter"] = value["parameter"]
    if "reason" in value:
        import aws_sdk_waf_regional.types.parameter_exception_reason

        out["reason"] = (
            aws_sdk_waf_regional.types.parameter_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInvalidParameterException_:
    out: WAFInvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "field" in data:
        import aws_sdk_waf_regional.types.parameter_exception_field

        out["field"] = (
            aws_sdk_waf_regional.types.parameter_exception_field.deserialize_aws_json_1_1(
                data["field"]
            )
        )
    if "parameter" in data:
        out["parameter"] = data["parameter"]
    if "reason" in data:
        import aws_sdk_waf_regional.types.parameter_exception_reason

        out["reason"] = (
            aws_sdk_waf_regional.types.parameter_exception_reason.deserialize_aws_json_1_1(
                data["reason"]
            )
        )
    return out


class WAFInvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFInvalidParameterException``."""

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
