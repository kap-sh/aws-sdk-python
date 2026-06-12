"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ServiceUnavailableException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_media_pipelines.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.error_code
    import aws_sdk_chime_sdk_media_pipelines.types.string


class ServiceUnavailableException_(TypedDict):
    code: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.string.String"]
    request_id: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.string.String"]
    """<p>The request ID associated with the call responsible for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
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


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
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


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmediapipelines#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(self, data: ServiceUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceUnavailableException":
        return cls(deserialize_json(data))
