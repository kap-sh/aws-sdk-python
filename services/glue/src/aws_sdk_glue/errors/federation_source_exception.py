"""Generated from Smithy shape ``com.amazonaws.glue#FederationSourceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_glue.types.federation_source_error_code
    import aws_sdk_glue.types.message_string


class FederationSourceException_(TypedDict, closed=True):
    federation_source_error_code: NotRequired[
        "aws_sdk_glue.types.federation_source_error_code.FederationSourceErrorCode"
    ]
    """<p>The error code of the problem.</p>"""
    message: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>The message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederationSourceException_) -> dict:
    out: dict = {}
    if "federation_source_error_code" in value:
        import aws_sdk_glue.types.federation_source_error_code

        out["FederationSourceErrorCode"] = (
            aws_sdk_glue.types.federation_source_error_code.serialize_aws_json_1_1(
                value["federation_source_error_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederationSourceException_:
    out: FederationSourceException_ = {}  # type: ignore[typeddict-item]
    if "FederationSourceErrorCode" in data:
        import aws_sdk_glue.types.federation_source_error_code

        out["federation_source_error_code"] = (
            aws_sdk_glue.types.federation_source_error_code.deserialize_aws_json_1_1(
                data["FederationSourceErrorCode"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FederationSourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#FederationSourceException``."""

    code: str | None = "FederationSourceException"

    def __init__(self, data: FederationSourceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FederationSourceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FederationSourceException":
        return cls(deserialize_aws_json_1_1(data))
