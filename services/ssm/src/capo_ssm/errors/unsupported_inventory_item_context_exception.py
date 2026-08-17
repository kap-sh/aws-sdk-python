"""Generated from Smithy shape ``com.amazonaws.ssm#UnsupportedInventoryItemContextException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.string


class UnsupportedInventoryItemContextException_(TypedDict, closed=True):
    type_name: NotRequired[
        "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    ]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedInventoryItemContextException_) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedInventoryItemContextException_:
    out: UnsupportedInventoryItemContextException_ = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnsupportedInventoryItemContextException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#UnsupportedInventoryItemContextException``."""

    code: str | None = "UnsupportedInventoryItemContextException"

    def __init__(
        self,
        data: UnsupportedInventoryItemContextException_,
        message: str | None = None,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedInventoryItemContextException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "UnsupportedInventoryItemContextException":
        return cls(deserialize_aws_json_1_1(data), message)
