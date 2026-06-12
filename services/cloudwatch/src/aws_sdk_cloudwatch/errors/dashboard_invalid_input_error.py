"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DashboardInvalidInputError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.dashboard_error_message
    import aws_sdk_cloudwatch.types.dashboard_validation_messages


class DashboardInvalidInputError_(TypedDict):
    message: NotRequired[
        "aws_sdk_cloudwatch.types.dashboard_error_message.DashboardErrorMessage"
    ]
    dashboard_validation_messages: NotRequired[
        "aws_sdk_cloudwatch.types.dashboard_validation_messages.DashboardValidationMessages"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardInvalidInputError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "dashboard_validation_messages" in value:
        import aws_sdk_cloudwatch.types.dashboard_validation_messages

        out["dashboardValidationMessages"] = (
            aws_sdk_cloudwatch.types.dashboard_validation_messages.serialize_aws_json_1_0(
                value["dashboard_validation_messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardInvalidInputError_:
    out: DashboardInvalidInputError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "dashboardValidationMessages" in data:
        import aws_sdk_cloudwatch.types.dashboard_validation_messages

        out["dashboard_validation_messages"] = (
            aws_sdk_cloudwatch.types.dashboard_validation_messages.deserialize_aws_json_1_0(
                data["dashboardValidationMessages"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DashboardInvalidInputError_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))
    if "dashboard_validation_messages" in value:
        import aws_sdk_cloudwatch.types.dashboard_validation_messages

        aws_sdk_cloudwatch.types.dashboard_validation_messages.serialize_query(
            value["dashboard_validation_messages"],
            pairs,
            f"{prefix}.dashboardValidationMessages",
        )


def deserialize_query(el: Element) -> DashboardInvalidInputError_:
    out: DashboardInvalidInputError_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_dashboard_validation_messages = el.find("dashboardValidationMessages")
    if child_dashboard_validation_messages is not None:
        import aws_sdk_cloudwatch.types.dashboard_validation_messages

        out["dashboard_validation_messages"] = (
            aws_sdk_cloudwatch.types.dashboard_validation_messages.deserialize_query(
                child_dashboard_validation_messages
            )
        )
    return out


class DashboardInvalidInputError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatch#DashboardInvalidInputError``."""

    code: str | None = "DashboardInvalidInputError"

    def __init__(self, data: DashboardInvalidInputError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DashboardInvalidInputError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "DashboardInvalidInputError":
        return cls(deserialize_aws_json_1_0(data))

    @classmethod
    def from_query(cls, el: Element) -> "DashboardInvalidInputError":
        return cls(deserialize_query(el))
