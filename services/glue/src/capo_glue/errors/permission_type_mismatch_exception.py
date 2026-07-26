"""Generated from Smithy shape ``com.amazonaws.glue#PermissionTypeMismatchException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class PermissionTypeMismatchException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>There is a mismatch between the SupportedPermissionType used in the query request and the permissions defined on the target table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionTypeMismatchException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PermissionTypeMismatchException_:
    out: PermissionTypeMismatchException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PermissionTypeMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#PermissionTypeMismatchException``."""

    code: str | None = "PermissionTypeMismatchException"

    def __init__(self, data: PermissionTypeMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PermissionTypeMismatchException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PermissionTypeMismatchException":
        return cls(deserialize_aws_json_1_1(data))
