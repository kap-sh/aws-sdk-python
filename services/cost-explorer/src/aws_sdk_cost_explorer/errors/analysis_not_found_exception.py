"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.error_message


class AnalysisNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisNotFoundException_:
    out: AnalysisNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AnalysisNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#AnalysisNotFoundException``."""

    code: str | None = "AnalysisNotFoundException"

    def __init__(self, data: AnalysisNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AnalysisNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AnalysisNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
