"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncCountExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ResourceDataSyncCountExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncCountExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncCountExceededException_:
    out: ResourceDataSyncCountExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceDataSyncCountExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourceDataSyncCountExceededException``."""

    code: str | None = "ResourceDataSyncCountExceededException"

    def __init__(self, data: ResourceDataSyncCountExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDataSyncCountExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceDataSyncCountExceededException":
        return cls(deserialize_aws_json_1_1(data))
