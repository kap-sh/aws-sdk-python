"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DataEncryptionException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.string


class DataEncryptionException_(TypedDict, closed=True):
    message: "aws_sdk_ssm_contacts.types.string.String"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataEncryptionException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataEncryptionException_:
    out: DataEncryptionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DataEncryptionException_.message required")
    return out


class DataEncryptionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmcontacts#DataEncryptionException``."""

    code: str | None = "DataEncryptionException"

    def __init__(self, data: DataEncryptionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DataEncryptionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DataEncryptionException":
        return cls(deserialize_aws_json_1_1(data))
