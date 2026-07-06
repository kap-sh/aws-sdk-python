"""Generated from Smithy shape ``com.amazonaws.ssm#GetInventorySchemaResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_item_schema_result_list
    import aws_sdk_ssm.types.next_token


class GetInventorySchemaResult(TypedDict, closed=True):
    schemas: NotRequired[
        "aws_sdk_ssm.types.inventory_item_schema_result_list.InventoryItemSchemaResultList"
    ]
    """<p>Inventory schemas returned by the request.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInventorySchemaResult) -> dict:
    out: dict = {}
    if "schemas" in value:
        import aws_sdk_ssm.types.inventory_item_schema_result_list

        out["Schemas"] = (
            aws_sdk_ssm.types.inventory_item_schema_result_list.serialize_aws_json_1_1(
                value["schemas"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInventorySchemaResult:
    out: GetInventorySchemaResult = {}  # type: ignore[typeddict-item]
    if "Schemas" in data:
        import aws_sdk_ssm.types.inventory_item_schema_result_list

        out["schemas"] = (
            aws_sdk_ssm.types.inventory_item_schema_result_list.deserialize_aws_json_1_1(
                data["Schemas"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
