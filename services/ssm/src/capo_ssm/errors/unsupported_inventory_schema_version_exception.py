"""Generated from Smithy shape ``com.amazonaws.ssm#UnsupportedInventorySchemaVersionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class UnsupportedInventorySchemaVersionException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedInventorySchemaVersionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedInventorySchemaVersionException_:
    out: UnsupportedInventorySchemaVersionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedInventorySchemaVersionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#UnsupportedInventorySchemaVersionException``."""

    code: str | None = "UnsupportedInventorySchemaVersionException"

    def __init__(self, data: UnsupportedInventorySchemaVersionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedInventorySchemaVersionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "UnsupportedInventorySchemaVersionException":
        return cls(deserialize_aws_json_1_1(data))
