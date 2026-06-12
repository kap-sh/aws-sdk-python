"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationConflictOperationFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_error_message


class IntegrationConflictOperationFault_(TypedDict):
    message: NotRequired[
        "aws_sdk_glue.types.integration_error_message.IntegrationErrorMessage"
    ]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationConflictOperationFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationConflictOperationFault_:
    out: IntegrationConflictOperationFault_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IntegrationConflictOperationFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#IntegrationConflictOperationFault``."""

    code: str | None = "IntegrationConflictOperationFault"

    def __init__(self, data: IntegrationConflictOperationFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IntegrationConflictOperationFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IntegrationConflictOperationFault":
        return cls(deserialize_aws_json_1_1(data))
