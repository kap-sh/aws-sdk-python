"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class OpsItemAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]
    ops_item_id: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemAlreadyExistsException_:
    out: OpsItemAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    return out


class OpsItemAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemAlreadyExistsException``."""

    code: str | None = "OpsItemAlreadyExistsException"

    def __init__(self, data: OpsItemAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OpsItemAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
