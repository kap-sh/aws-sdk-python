"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskStoppingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string


class MaterializedViewRefreshTaskStoppingException_(TypedDict):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaterializedViewRefreshTaskStoppingException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> MaterializedViewRefreshTaskStoppingException_:
    out: MaterializedViewRefreshTaskStoppingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MaterializedViewRefreshTaskStoppingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskStoppingException``."""

    code: str | None = "MaterializedViewRefreshTaskStoppingException"

    def __init__(self, data: MaterializedViewRefreshTaskStoppingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaterializedViewRefreshTaskStoppingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "MaterializedViewRefreshTaskStoppingException":
        return cls(deserialize_aws_json_1_1(data))
