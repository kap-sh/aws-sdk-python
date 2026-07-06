"""Generated from Smithy shape ``com.amazonaws.glue#InvalidInputException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.message_string
    import aws_sdk_glue.types.nullable_boolean


class InvalidInputException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""
    from_federation_source: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether or not the exception relates to a federated source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInputException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "from_federation_source" in value:
        out["FromFederationSource"] = value["from_federation_source"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "FromFederationSource" in data:
        out["from_federation_source"] = data["FromFederationSource"]
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(self, data: InvalidInputException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInputException":
        return cls(deserialize_aws_json_1_1(data))
