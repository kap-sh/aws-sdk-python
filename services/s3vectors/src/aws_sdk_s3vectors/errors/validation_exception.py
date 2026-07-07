"""Generated from Smithy shape ``com.amazonaws.s3vectors#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.validation_exception_field_list


class ValidationException_(TypedDict, closed=True):
    message: "str"
    field_list: NotRequired[
        "aws_sdk_s3vectors.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of specific validation failures that are encountered during input processing. Each entry in the list contains a path to the field that failed validation and a detailed message that explains why the validation failed. To satisfy multiple constraints, a field can appear multiple times in this list if it failed. You can use the information to identify and fix the specific validation issues in your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "field_list" in value:
        import aws_sdk_s3vectors.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_s3vectors.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "fieldList" in data:
        import aws_sdk_s3vectors.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_s3vectors.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#ValidationException``."""

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
