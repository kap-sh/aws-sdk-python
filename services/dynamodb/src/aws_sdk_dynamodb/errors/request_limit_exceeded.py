"""Generated from Smithy shape ``com.amazonaws.dynamodb#RequestLimitExceeded``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message
    import aws_sdk_dynamodb.types.throttling_reason_list


class RequestLimitExceeded_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]
    throttling_reasons: NotRequired[
        "aws_sdk_dynamodb.types.throttling_reason_list.ThrottlingReasonList"
    ]
    r"""<p>A list of <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html\">ThrottlingReason</a> that provide detailed diagnostic information about why the request was throttled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "throttling_reasons" in value:
        import aws_sdk_dynamodb.types.throttling_reason_list

        out["ThrottlingReasons"] = (
            aws_sdk_dynamodb.types.throttling_reason_list.serialize_aws_json_1_0(
                value["throttling_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestLimitExceeded_:
    out: RequestLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "ThrottlingReasons" in data:
        import aws_sdk_dynamodb.types.throttling_reason_list

        out["throttling_reasons"] = (
            aws_sdk_dynamodb.types.throttling_reason_list.deserialize_aws_json_1_0(
                data["ThrottlingReasons"]
            )
        )
    return out


class RequestLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#RequestLimitExceeded``."""

    code: str | None = "RequestLimitExceeded"

    def __init__(self, data: RequestLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "RequestLimitExceeded":
        return cls(deserialize_aws_json_1_0(data))
