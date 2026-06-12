"""Generated from Smithy shape ``com.amazonaws.ssm#ItemContentMismatchException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_type_name
    import aws_sdk_ssm.types.string


class ItemContentMismatchException_(TypedDict):
    type_name: NotRequired[
        "aws_sdk_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ItemContentMismatchException_) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ItemContentMismatchException_:
    out: ItemContentMismatchException_ = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ItemContentMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ItemContentMismatchException``."""

    code: str | None = "ItemContentMismatchException"

    def __init__(self, data: ItemContentMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ItemContentMismatchException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ItemContentMismatchException":
        return cls(deserialize_aws_json_1_1(data))
