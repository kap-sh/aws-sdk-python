"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DashboardNotFoundError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.dashboard_error_message


class DashboardNotFoundError_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_cloudwatch.types.dashboard_error_message.DashboardErrorMessage"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardNotFoundError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardNotFoundError_:
    out: DashboardNotFoundError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DashboardNotFoundError_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DashboardNotFoundError_:
    out: DashboardNotFoundError_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DashboardNotFoundError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatch#DashboardNotFoundError``."""

    code: str | None = "DashboardNotFoundError"

    def __init__(self, data: DashboardNotFoundError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DashboardNotFoundError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "DashboardNotFoundError":
        return cls(deserialize_aws_json_1_0(data))

    @classmethod
    def from_query(cls, el: Element) -> "DashboardNotFoundError":
        return cls(deserialize_query(el))
