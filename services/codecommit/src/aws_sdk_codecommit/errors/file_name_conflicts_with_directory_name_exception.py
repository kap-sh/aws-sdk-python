"""Generated from Smithy shape ``com.amazonaws.codecommit#FileNameConflictsWithDirectoryNameException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class FileNameConflictsWithDirectoryNameException_(TypedDict):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileNameConflictsWithDirectoryNameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> FileNameConflictsWithDirectoryNameException_:
    out: FileNameConflictsWithDirectoryNameException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class FileNameConflictsWithDirectoryNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#FileNameConflictsWithDirectoryNameException``."""

    code: str | None = "FileNameConflictsWithDirectoryNameException"

    def __init__(self, data: FileNameConflictsWithDirectoryNameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FileNameConflictsWithDirectoryNameException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "FileNameConflictsWithDirectoryNameException":
        return cls(deserialize_aws_json_1_1(data))
