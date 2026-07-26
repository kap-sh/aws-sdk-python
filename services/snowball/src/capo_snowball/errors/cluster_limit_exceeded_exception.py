"""Generated from Smithy shape ``com.amazonaws.snowball#ClusterLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import ServiceError

if TYPE_CHECKING:
    import capo_snowball.types.string


class ClusterLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterLimitExceededException_:
    out: ClusterLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ClusterLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#ClusterLimitExceededException``."""

    code: str | None = "ClusterLimitExceededException"

    def __init__(self, data: ClusterLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ClusterLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
