"""Generated from Smithy shape ``com.amazonaws.ssm#CreateOpsItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_arn
    import capo_ssm.types.string


class CreateOpsItemResponse(TypedDict, closed=True):
    ops_item_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of the OpsItem.</p>"""
    ops_item_arn: NotRequired["capo_ssm.types.ops_item_arn.OpsItemArn"]
    """<p>The OpsItem Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOpsItemResponse) -> dict:
    out: dict = {}
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "ops_item_arn" in value:
        out["OpsItemArn"] = value["ops_item_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOpsItemResponse:
    out: CreateOpsItemResponse = {}  # type: ignore[typeddict-item]
    if "OpsItemId" in data:
        out["ops_item_id"] = data["OpsItemId"]
    if "OpsItemArn" in data:
        out["ops_item_arn"] = data["OpsItemArn"]
    return out
