"""Generated from Smithy shape ``com.amazonaws.glue#FederatedResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn
    import aws_sdk_glue.types.message_string


class FederatedResourceAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>The message describing the problem.</p>"""
    associated_glue_resource: NotRequired[
        "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"
    ]
    """<p>The associated Glue resource already exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederatedResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "associated_glue_resource" in value:
        out["AssociatedGlueResource"] = value["associated_glue_resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederatedResourceAlreadyExistsException_:
    out: FederatedResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "AssociatedGlueResource" in data:
        out["associated_glue_resource"] = data["AssociatedGlueResource"]
    return out


class FederatedResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#FederatedResourceAlreadyExistsException``."""

    code: str | None = "FederatedResourceAlreadyExistsException"

    def __init__(self, data: FederatedResourceAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FederatedResourceAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FederatedResourceAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
