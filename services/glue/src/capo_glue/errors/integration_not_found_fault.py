"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.integration_error_message


class IntegrationNotFoundFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_glue.types.integration_error_message.IntegrationErrorMessage"
    ]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationNotFoundFault_:
    out: IntegrationNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IntegrationNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#IntegrationNotFoundFault``."""

    code: str | None = "IntegrationNotFoundFault"

    def __init__(self, data: IntegrationNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IntegrationNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IntegrationNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
