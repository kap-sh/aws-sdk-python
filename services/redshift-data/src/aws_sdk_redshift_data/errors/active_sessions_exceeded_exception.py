"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ActiveSessionsExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string


class ActiveSessionsExceededException_(TypedDict):
    message: NotRequired["aws_sdk_redshift_data.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveSessionsExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActiveSessionsExceededException_:
    out: ActiveSessionsExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ActiveSessionsExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftdata#ActiveSessionsExceededException``."""

    code: str | None = "ActiveSessionsExceededException"

    def __init__(self, data: ActiveSessionsExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ActiveSessionsExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ActiveSessionsExceededException":
        return cls(deserialize_aws_json_1_1(data))
