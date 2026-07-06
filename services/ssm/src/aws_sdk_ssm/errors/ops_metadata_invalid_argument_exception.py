"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataInvalidArgumentException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class OpsMetadataInvalidArgumentException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataInvalidArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsMetadataInvalidArgumentException_:
    out: OpsMetadataInvalidArgumentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OpsMetadataInvalidArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsMetadataInvalidArgumentException``."""

    code: str | None = "OpsMetadataInvalidArgumentException"

    def __init__(self, data: OpsMetadataInvalidArgumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsMetadataInvalidArgumentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OpsMetadataInvalidArgumentException":
        return cls(deserialize_aws_json_1_1(data))
