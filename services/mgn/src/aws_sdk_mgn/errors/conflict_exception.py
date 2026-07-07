"""Generated from Smithy shape ``com.amazonaws.mgn#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.conflict_exception_errors
    import aws_sdk_mgn.types.large_bounded_string


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"]
    resource_id: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>A conflict occurred when prompting for the Resource ID.</p>"""
    resource_type: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>A conflict occurred when prompting for resource type.</p>"""
    errors: NotRequired[
        "aws_sdk_mgn.types.conflict_exception_errors.ConflictExceptionErrors"
    ]
    """<p>Conflict Exception specific errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "errors" in value:
        import aws_sdk_mgn.types.conflict_exception_errors

        out["errors"] = aws_sdk_mgn.types.conflict_exception_errors.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "errors" in data:
        import aws_sdk_mgn.types.conflict_exception_errors

        out["errors"] = aws_sdk_mgn.types.conflict_exception_errors.deserialize_json(
            data["errors"]
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#ConflictException``."""

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
