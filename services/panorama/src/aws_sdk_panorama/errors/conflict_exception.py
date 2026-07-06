"""Generated from Smithy shape ``com.amazonaws.panorama#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.conflict_exception_error_argument_list
    import aws_sdk_panorama.types.string


class ConflictException_(TypedDict, closed=True):
    message: "aws_sdk_panorama.types.string.String"
    resource_id: "aws_sdk_panorama.types.string.String"
    """<p>The resource's ID.</p>"""
    resource_type: "aws_sdk_panorama.types.string.String"
    """<p>The resource's type.</p>"""
    error_id: NotRequired["aws_sdk_panorama.types.string.String"]
    """<p>A unique ID for the error.</p>"""
    error_arguments: NotRequired[
        "aws_sdk_panorama.types.conflict_exception_error_argument_list.ConflictExceptionErrorArgumentList"
    ]
    """<p>A list of attributes that led to the exception and their values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "error_id" in value:
        out["ErrorId"] = value["error_id"]
    if "error_arguments" in value:
        import aws_sdk_panorama.types.conflict_exception_error_argument_list

        out["ErrorArguments"] = (
            aws_sdk_panorama.types.conflict_exception_error_argument_list.serialize_json(
                value["error_arguments"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    if "ErrorId" in data:
        out["error_id"] = data["ErrorId"]
    if "ErrorArguments" in data:
        import aws_sdk_panorama.types.conflict_exception_error_argument_list

        out["error_arguments"] = (
            aws_sdk_panorama.types.conflict_exception_error_argument_list.deserialize_json(
                data["ErrorArguments"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.panorama#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
