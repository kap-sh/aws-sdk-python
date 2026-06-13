"""Generated from Smithy shape ``com.amazonaws.devopsagent#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.validation_exception_field_list


class ValidationException_(TypedDict):
    message: "str"
    """<p>A summary of the validation failure.</p>"""
    field_list: NotRequired[
        "aws_sdk_devops_agent.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "field_list" in value:
        import aws_sdk_devops_agent.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_devops_agent.types.validation_exception_field_list.serialize_json(
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
        import aws_sdk_devops_agent.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_devops_agent.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsagent#ValidationException``."""

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
