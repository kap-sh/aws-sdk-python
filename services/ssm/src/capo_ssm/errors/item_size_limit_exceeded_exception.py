"""Generated from Smithy shape ``com.amazonaws.ssm#ItemSizeLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.string


class ItemSizeLimitExceededException_(TypedDict, closed=True):
    type_name: NotRequired[
        "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ItemSizeLimitExceededException_) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ItemSizeLimitExceededException_:
    out: ItemSizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ItemSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ItemSizeLimitExceededException``."""

    code: str | None = "ItemSizeLimitExceededException"

    def __init__(self, data: ItemSizeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ItemSizeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ItemSizeLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
