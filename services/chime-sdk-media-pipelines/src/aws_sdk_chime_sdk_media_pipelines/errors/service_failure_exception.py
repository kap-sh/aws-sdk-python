"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ServiceFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.error_code
    import aws_sdk_chime_sdk_media_pipelines.types.string


class ServiceFailureException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.string.String"]
    request_id: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.string.String"]
    """<p>The request ID associated with the call responsible for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFailureException_) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.error_code

        out["Code"] = aws_sdk_chime_sdk_media_pipelines.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ServiceFailureException_:
    out: ServiceFailureException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.error_code

        out["code"] = (
            aws_sdk_chime_sdk_media_pipelines.types.error_code.deserialize_json(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class ServiceFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmediapipelines#ServiceFailureException``."""

    code: str | None = "ServiceFailureException"

    def __init__(self, data: ServiceFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceFailureException":
        return cls(deserialize_json(data))
