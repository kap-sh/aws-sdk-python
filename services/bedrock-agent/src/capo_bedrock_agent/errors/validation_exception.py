"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.non_blank_string
    import capo_bedrock_agent.types.validation_exception_field_list


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_bedrock_agent.types.non_blank_string.NonBlankString"]
    field_list: NotRequired[
        "capo_bedrock_agent.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of objects containing fields that caused validation errors and their corresponding validation error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "field_list" in value:
        import capo_bedrock_agent.types.validation_exception_field_list

        out["fieldList"] = (
            capo_bedrock_agent.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "fieldList" in data:
        import capo_bedrock_agent.types.validation_exception_field_list

        out["field_list"] = (
            capo_bedrock_agent.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagent#ValidationException``."""

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
