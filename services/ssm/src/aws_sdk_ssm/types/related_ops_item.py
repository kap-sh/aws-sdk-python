"""Generated from Smithy shape ``com.amazonaws.ssm#RelatedOpsItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class RelatedOpsItem(TypedDict):
    ops_item_id: "aws_sdk_ssm.types.string.String"
    """<p>The ID of an OpsItem related to the current OpsItem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedOpsItem) -> dict:
    out: dict = {}
    out["OpsItemId"] = value["ops_item_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelatedOpsItem:
    out: RelatedOpsItem = {}  # type: ignore[typeddict-item]
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    else:
        raise DeserializationError("RelatedOpsItem.ops_item_id required")
    return out
