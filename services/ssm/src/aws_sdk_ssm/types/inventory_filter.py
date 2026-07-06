"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_filter_key
    import aws_sdk_ssm.types.inventory_filter_value_list
    import aws_sdk_ssm.types.inventory_query_operator_type


class InventoryFilter(TypedDict, closed=True):
    key: "aws_sdk_ssm.types.inventory_filter_key.InventoryFilterKey"
    """<p>The name of the filter key.</p>"""
    values: "aws_sdk_ssm.types.inventory_filter_value_list.InventoryFilterValueList"
    """<p>Inventory filter values.</p>"""
    type: NotRequired[
        "aws_sdk_ssm.types.inventory_query_operator_type.InventoryQueryOperatorType"
    ]
    r"""<p>The type of filter.</p> <note> <p>The <code>Exists</code> filter must be used with aggregators. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-aggregate.html\">Aggregating inventory data</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_ssm.types.inventory_filter_value_list

    out["Values"] = (
        aws_sdk_ssm.types.inventory_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    if "type" in value:
        import aws_sdk_ssm.types.inventory_query_operator_type

        out["Type"] = (
            aws_sdk_ssm.types.inventory_query_operator_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryFilter:
    out: InventoryFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("InventoryFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.inventory_filter_value_list

        out["values"] = (
            aws_sdk_ssm.types.inventory_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("InventoryFilter.values required")
    if "Type" in data:
        import aws_sdk_ssm.types.inventory_query_operator_type

        out["type"] = (
            aws_sdk_ssm.types.inventory_query_operator_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
