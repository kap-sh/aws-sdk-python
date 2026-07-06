"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#TooManyTagsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.amazon_resource_name
    import aws_sdk_application_auto_scaling.types.exception_message


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_application_auto_scaling.types.exception_message.ExceptionMessage"
    ]
    resource_name: NotRequired[
        "aws_sdk_application_auto_scaling.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The name of the Application Auto Scaling resource. This value is an Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationautoscaling#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(self, data: TooManyTagsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TooManyTagsException":
        return cls(deserialize_aws_json_1_1(data))
