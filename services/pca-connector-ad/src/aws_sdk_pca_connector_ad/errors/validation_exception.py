"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pca_connector_ad.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "str"
    reason: NotRequired[
        "aws_sdk_pca_connector_ad.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the validation error. This won't be return for every validation exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_pca_connector_ad.types.validation_exception_reason

        out["Reason"] = (
            aws_sdk_pca_connector_ad.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "Reason" in data:
        import aws_sdk_pca_connector_ad.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_pca_connector_ad.types.validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pcaconnectorad#ValidationException``."""

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
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))
