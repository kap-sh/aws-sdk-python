"""Generated from Smithy shape ``com.amazonaws.uxc#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_uxc.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_uxc.types.validation_exception_field_list


class ValidationException_(TypedDict, closed=True):
    message: "str"
    field_list: NotRequired[
        "capo_uxc.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The list of fields that are invalid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "field_list" in value:
        import capo_uxc.types.validation_exception_field_list

        out["fieldList"] = (
            capo_uxc.types.validation_exception_field_list.serialize_json(
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
        import capo_uxc.types.validation_exception_field_list

        out["field_list"] = (
            capo_uxc.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.uxc#ValidationException``."""

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
