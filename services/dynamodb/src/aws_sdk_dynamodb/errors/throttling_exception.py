"""Generated from Smithy shape ``com.amazonaws.dynamodb#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.availability_error_message
    import aws_sdk_dynamodb.types.throttling_reason_list


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_dynamodb.types.availability_error_message.AvailabilityErrorMessage"
    ]
    throttling_reasons: NotRequired[
        "aws_sdk_dynamodb.types.throttling_reason_list.ThrottlingReasonList"
    ]
    r"""<p>A list of <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html\">ThrottlingReason</a> that provide detailed diagnostic information about why the request was throttled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "throttling_reasons" in value:
        import aws_sdk_dynamodb.types.throttling_reason_list

        out["throttlingReasons"] = (
            aws_sdk_dynamodb.types.throttling_reason_list.serialize_aws_json_1_0(
                value["throttling_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "throttlingReasons" in data:
        import aws_sdk_dynamodb.types.throttling_reason_list

        out["throttling_reasons"] = (
            aws_sdk_dynamodb.types.throttling_reason_list.deserialize_aws_json_1_0(
                data["throttlingReasons"]
            )
        )
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data))
