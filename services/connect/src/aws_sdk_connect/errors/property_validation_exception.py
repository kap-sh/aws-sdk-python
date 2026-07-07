"""Generated from Smithy shape ``com.amazonaws.connect#PropertyValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.message
    import aws_sdk_connect.types.property_validation_exception_property_list


class PropertyValidationException_(TypedDict, closed=True):
    message: "aws_sdk_connect.types.message.Message"
    property_list: NotRequired[
        "aws_sdk_connect.types.property_validation_exception_property_list.PropertyValidationExceptionPropertyList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "property_list" in value:
        import aws_sdk_connect.types.property_validation_exception_property_list

        out["PropertyList"] = (
            aws_sdk_connect.types.property_validation_exception_property_list.serialize_json(
                value["property_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> PropertyValidationException_:
    out: PropertyValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("PropertyValidationException_.message required")
    if "PropertyList" in data:
        import aws_sdk_connect.types.property_validation_exception_property_list

        out["property_list"] = (
            aws_sdk_connect.types.property_validation_exception_property_list.deserialize_json(
                data["PropertyList"]
            )
        )
    return out


class PropertyValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#PropertyValidationException``."""

    code: str | None = "PropertyValidationException"

    def __init__(self, data: PropertyValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PropertyValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PropertyValidationException":
        return cls(deserialize_json(data))
