"""Generated from Smithy shape ``com.amazonaws.glue#TargetResourceNotFound``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_error_message


class TargetResourceNotFound_(TypedDict):
    message: NotRequired[
        "aws_sdk_glue.types.integration_error_message.IntegrationErrorMessage"
    ]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetResourceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetResourceNotFound_:
    out: TargetResourceNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TargetResourceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#TargetResourceNotFound``."""

    code: str | None = "TargetResourceNotFound"

    def __init__(self, data: TargetResourceNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TargetResourceNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TargetResourceNotFound":
        return cls(deserialize_aws_json_1_1(data))
