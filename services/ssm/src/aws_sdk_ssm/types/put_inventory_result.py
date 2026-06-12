"""Generated from Smithy shape ``com.amazonaws.ssm#PutInventoryResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.put_inventory_message


class PutInventoryResult(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.put_inventory_message.PutInventoryMessage"]
    """<p>Information about the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInventoryResult) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInventoryResult:
    out: PutInventoryResult = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
