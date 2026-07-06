"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskNotRunningException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class MaterializedViewRefreshTaskNotRunningException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaterializedViewRefreshTaskNotRunningException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> MaterializedViewRefreshTaskNotRunningException_:
    out: MaterializedViewRefreshTaskNotRunningException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MaterializedViewRefreshTaskNotRunningException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskNotRunningException``."""

    code: str | None = "MaterializedViewRefreshTaskNotRunningException"

    def __init__(self, data: MaterializedViewRefreshTaskNotRunningException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaterializedViewRefreshTaskNotRunningException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "MaterializedViewRefreshTaskNotRunningException":
        return cls(deserialize_aws_json_1_1(data))
