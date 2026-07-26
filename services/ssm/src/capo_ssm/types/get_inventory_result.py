"""Generated from Smithy shape ``com.amazonaws.ssm#GetInventoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_result_entity_list
    import capo_ssm.types.next_token


class GetInventoryResult(TypedDict, closed=True):
    entities: NotRequired[
        "capo_ssm.types.inventory_result_entity_list.InventoryResultEntityList"
    ]
    """<p>Collection of inventory entities such as a collection of managed node inventory. </p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInventoryResult) -> dict:
    out: dict = {}
    if "entities" in value:
        import capo_ssm.types.inventory_result_entity_list

        out["Entities"] = (
            capo_ssm.types.inventory_result_entity_list.serialize_aws_json_1_1(
                value["entities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInventoryResult:
    out: GetInventoryResult = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import capo_ssm.types.inventory_result_entity_list

        out["entities"] = (
            capo_ssm.types.inventory_result_entity_list.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
