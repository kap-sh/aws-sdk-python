"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataKeyLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class OpsMetadataKeyLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataKeyLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsMetadataKeyLimitExceededException_:
    out: OpsMetadataKeyLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OpsMetadataKeyLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsMetadataKeyLimitExceededException``."""

    code: str | None = "OpsMetadataKeyLimitExceededException"

    def __init__(
        self, data: OpsMetadataKeyLimitExceededException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsMetadataKeyLimitExceededException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "OpsMetadataKeyLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message)
