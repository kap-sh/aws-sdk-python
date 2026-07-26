"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsufficientIAMAccessPermissionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message


class InsufficientIAMAccessPermissionException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsufficientIAMAccessPermissionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InsufficientIAMAccessPermissionException_:
    out: InsufficientIAMAccessPermissionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InsufficientIAMAccessPermissionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InsufficientIAMAccessPermissionException``."""

    code: str | None = "InsufficientIAMAccessPermissionException"

    def __init__(self, data: InsufficientIAMAccessPermissionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientIAMAccessPermissionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InsufficientIAMAccessPermissionException":
        return cls(deserialize_aws_json_1_1(data))
