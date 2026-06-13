"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resource_explorer_2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.validation_exception_field_list


class ValidationException_(TypedDict):
    message: "str"
    field_list: NotRequired[
        "aws_sdk_resource_explorer_2.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>An array of the request fields that had validation errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "field_list" in value:
        import aws_sdk_resource_explorer_2.types.validation_exception_field_list

        out["FieldList"] = (
            aws_sdk_resource_explorer_2.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "FieldList" in data:
        import aws_sdk_resource_explorer_2.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_resource_explorer_2.types.validation_exception_field_list.deserialize_json(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourceexplorer2#ValidationException``."""

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
