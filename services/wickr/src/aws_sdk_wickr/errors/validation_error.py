"""Generated from Smithy shape ``com.amazonaws.wickr#ValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.error_detail_list
    import aws_sdk_wickr.types.generic_string


class ValidationError_(TypedDict, closed=True):
    reasons: NotRequired["aws_sdk_wickr.types.error_detail_list.ErrorDetailList"]
    """<p>A list of validation error details, where each item identifies a specific field that failed validation and explains the reason for the failure.</p>"""
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message describing the validation error error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationError_) -> dict:
    out: dict = {}
    if "reasons" in value:
        import aws_sdk_wickr.types.error_detail_list

        out["reasons"] = aws_sdk_wickr.types.error_detail_list.serialize_json(
            value["reasons"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationError_:
    out: ValidationError_ = {}  # type: ignore[typeddict-item]
    if "reasons" in data:
        import aws_sdk_wickr.types.error_detail_list

        out["reasons"] = aws_sdk_wickr.types.error_detail_list.deserialize_json(
            data["reasons"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out


class ValidationError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#ValidationError``."""

    code: str | None = "ValidationError"

    def __init__(self, data: ValidationError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationError":
        return cls(deserialize_json(data))
