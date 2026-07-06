"""Generated from Smithy shape ``com.amazonaws.codecommit#EncryptionKeyDisabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class EncryptionKeyDisabledException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKeyDisabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionKeyDisabledException_:
    out: EncryptionKeyDisabledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class EncryptionKeyDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#EncryptionKeyDisabledException``."""

    code: str | None = "EncryptionKeyDisabledException"

    def __init__(self, data: EncryptionKeyDisabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionKeyDisabledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EncryptionKeyDisabledException":
        return cls(deserialize_aws_json_1_1(data))
