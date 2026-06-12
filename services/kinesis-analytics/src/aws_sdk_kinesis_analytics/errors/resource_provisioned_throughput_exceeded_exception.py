"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ResourceProvisionedThroughputExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.error_message


class ResourceProvisionedThroughputExceededException_(TypedDict):
    message: NotRequired["aws_sdk_kinesis_analytics.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ResourceProvisionedThroughputExceededException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ResourceProvisionedThroughputExceededException_:
    out: ResourceProvisionedThroughputExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceProvisionedThroughputExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisanalytics#ResourceProvisionedThroughputExceededException``."""

    code: str | None = "ResourceProvisionedThroughputExceededException"

    def __init__(self, data: ResourceProvisionedThroughputExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceProvisionedThroughputExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "ResourceProvisionedThroughputExceededException":
        return cls(deserialize_aws_json_1_1(data))
