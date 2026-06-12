"""Generated from Smithy shape ``com.amazonaws.ssm#GetInventoryResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_result_entity_list
    import aws_sdk_ssm.types.next_token


class GetInventoryResult(TypedDict):
    entities: NotRequired[
        "aws_sdk_ssm.types.inventory_result_entity_list.InventoryResultEntityList"
    ]
    """<p>Collection of inventory entities such as a collection of managed node inventory. </p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInventoryResult) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_ssm.types.inventory_result_entity_list

        out["Entities"] = (
            aws_sdk_ssm.types.inventory_result_entity_list.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInventoryResult:
    out: GetInventoryResult = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import aws_sdk_ssm.types.inventory_result_entity_list

        out["entities"] = (
            aws_sdk_ssm.types.inventory_result_entity_list.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
