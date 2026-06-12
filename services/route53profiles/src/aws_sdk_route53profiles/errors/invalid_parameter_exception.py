"""Generated from Smithy shape ``com.amazonaws.route53profiles#InvalidParameterException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53profiles.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.exception_message
    import aws_sdk_route53profiles.types.string


class InvalidParameterException_(TypedDict):
    message: "aws_sdk_route53profiles.types.exception_message.ExceptionMessage"
    field_name: NotRequired["aws_sdk_route53profiles.types.string.String"]
    """<p> The parameter field name for the invalid parameter exception. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    return out


def deserialize_json(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InvalidParameterException_.message required")
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53profiles#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(self, data: InvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterException":
        return cls(deserialize_json(data))
