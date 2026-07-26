"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskRunningException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class MaterializedViewRefreshTaskRunningException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaterializedViewRefreshTaskRunningException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> MaterializedViewRefreshTaskRunningException_:
    out: MaterializedViewRefreshTaskRunningException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MaterializedViewRefreshTaskRunningException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskRunningException``."""

    code: str | None = "MaterializedViewRefreshTaskRunningException"

    def __init__(self, data: MaterializedViewRefreshTaskRunningException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaterializedViewRefreshTaskRunningException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "MaterializedViewRefreshTaskRunningException":
        return cls(deserialize_aws_json_1_1(data))
