"""Generated from Smithy shape ``com.amazonaws.codecommit#EncryptionKeyNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class EncryptionKeyNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKeyNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionKeyNotFoundException_:
    out: EncryptionKeyNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class EncryptionKeyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#EncryptionKeyNotFoundException``."""

    code: str | None = "EncryptionKeyNotFoundException"

    def __init__(self, data: EncryptionKeyNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionKeyNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EncryptionKeyNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
