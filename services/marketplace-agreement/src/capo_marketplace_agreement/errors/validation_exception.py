"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.exception_message
    import capo_marketplace_agreement.types.request_id
    import capo_marketplace_agreement.types.validation_exception_field_list
    import capo_marketplace_agreement.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    request_id: NotRequired["capo_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier associated with the error.</p>"""
    message: NotRequired[
        "capo_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""
    reason: NotRequired[
        "capo_marketplace_agreement.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason associated with the error.</p>"""
    fields: NotRequired[
        "capo_marketplace_agreement.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The fields associated with the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import capo_marketplace_agreement.types.validation_exception_reason

        out["reason"] = (
            capo_marketplace_agreement.types.validation_exception_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    if "fields" in value:
        import capo_marketplace_agreement.types.validation_exception_field_list

        out["fields"] = (
            capo_marketplace_agreement.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "message" in data:
        out["message"] = data["message"]
    if "reason" in data:
        import capo_marketplace_agreement.types.validation_exception_reason

        out["reason"] = (
            capo_marketplace_agreement.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    if "fields" in data:
        import capo_marketplace_agreement.types.validation_exception_field_list

        out["fields"] = (
            capo_marketplace_agreement.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#ValidationException``."""

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
