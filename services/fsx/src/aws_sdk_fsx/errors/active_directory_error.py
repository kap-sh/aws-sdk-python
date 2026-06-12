"""Generated from Smithy shape ``com.amazonaws.fsx#ActiveDirectoryError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.active_directory_error_type
    import aws_sdk_fsx.types.directory_id
    import aws_sdk_fsx.types.error_message


class ActiveDirectoryError_(TypedDict):
    active_directory_id: NotRequired["aws_sdk_fsx.types.directory_id.DirectoryId"]
    """<p>The directory ID of the directory that an error pertains to.</p>"""
    type: NotRequired[
        "aws_sdk_fsx.types.active_directory_error_type.ActiveDirectoryErrorType"
    ]
    """<p>The type of Active Directory error.</p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveDirectoryError_) -> dict:
    out: dict = {}
    if "active_directory_id" in value:
        out["ActiveDirectoryId"] = value["active_directory_id"]
    if "type" in value:
        import aws_sdk_fsx.types.active_directory_error_type

        out["Type"] = (
            aws_sdk_fsx.types.active_directory_error_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActiveDirectoryError_:
    out: ActiveDirectoryError_ = {}  # type: ignore[typeddict-item]
    if "ActiveDirectoryId" in data:
        out["active_directory_id"] = data["ActiveDirectoryId"]
    if "Type" in data:
        import aws_sdk_fsx.types.active_directory_error_type

        out["type"] = (
            aws_sdk_fsx.types.active_directory_error_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ActiveDirectoryError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#ActiveDirectoryError``."""

    code: str | None = "ActiveDirectoryError"

    def __init__(self, data: ActiveDirectoryError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ActiveDirectoryError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ActiveDirectoryError":
        return cls(deserialize_aws_json_1_1(data))
