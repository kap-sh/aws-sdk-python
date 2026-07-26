"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#NotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.error_code
    import capo_chime_sdk_media_pipelines.types.string


class NotFoundException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_media_pipelines.types.error_code.ErrorCode"]
    message: NotRequired["capo_chime_sdk_media_pipelines.types.string.String"]
    request_id: NotRequired["capo_chime_sdk_media_pipelines.types.string.String"]
    """<p>The request ID associated with the call responsible for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_chime_sdk_media_pipelines.types.error_code

        out["Code"] = capo_chime_sdk_media_pipelines.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_chime_sdk_media_pipelines.types.error_code

        out["code"] = capo_chime_sdk_media_pipelines.types.error_code.deserialize_json(
            data["Code"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmediapipelines#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_json(data))
