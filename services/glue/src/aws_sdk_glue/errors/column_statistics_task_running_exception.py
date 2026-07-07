"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsTaskRunningException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class ColumnStatisticsTaskRunningException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsTaskRunningException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnStatisticsTaskRunningException_:
    out: ColumnStatisticsTaskRunningException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ColumnStatisticsTaskRunningException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#ColumnStatisticsTaskRunningException``."""

    code: str | None = "ColumnStatisticsTaskRunningException"

    def __init__(self, data: ColumnStatisticsTaskRunningException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ColumnStatisticsTaskRunningException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ColumnStatisticsTaskRunningException":
        return cls(deserialize_aws_json_1_1(data))
