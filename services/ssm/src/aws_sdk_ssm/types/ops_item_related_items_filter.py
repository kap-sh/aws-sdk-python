"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_related_items_filter_key
    import aws_sdk_ssm.types.ops_item_related_items_filter_operator
    import aws_sdk_ssm.types.ops_item_related_items_filter_values


class OpsItemRelatedItemsFilter(TypedDict):
    key: "aws_sdk_ssm.types.ops_item_related_items_filter_key.OpsItemRelatedItemsFilterKey"
    """<p>The name of the filter key. Supported values include <code>ResourceUri</code>, <code>ResourceType</code>, or <code>AssociationId</code>.</p>"""
    values: "aws_sdk_ssm.types.ops_item_related_items_filter_values.OpsItemRelatedItemsFilterValues"
    """<p>The values for the filter.</p>"""
    operator: "aws_sdk_ssm.types.ops_item_related_items_filter_operator.OpsItemRelatedItemsFilterOperator"
    """<p>The operator used by the filter call. The only supported operator is <code>EQUAL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.ops_item_related_items_filter_key

    out["Key"] = (
        aws_sdk_ssm.types.ops_item_related_items_filter_key.serialize_aws_json_1_1(
            value["key"]
        )
    )
    import aws_sdk_ssm.types.ops_item_related_items_filter_values

    out["Values"] = (
        aws_sdk_ssm.types.ops_item_related_items_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import aws_sdk_ssm.types.ops_item_related_items_filter_operator

    out["Operator"] = (
        aws_sdk_ssm.types.ops_item_related_items_filter_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemRelatedItemsFilter:
    out: OpsItemRelatedItemsFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_ssm.types.ops_item_related_items_filter_key

        out["key"] = (
            aws_sdk_ssm.types.ops_item_related_items_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    else:
        raise DeserializationError("OpsItemRelatedItemsFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.ops_item_related_items_filter_values

        out["values"] = (
            aws_sdk_ssm.types.ops_item_related_items_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("OpsItemRelatedItemsFilter.values required")
    if "Operator" in data:
        import aws_sdk_ssm.types.ops_item_related_items_filter_operator

        out["operator"] = (
            aws_sdk_ssm.types.ops_item_related_items_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("OpsItemRelatedItemsFilter.operator required")
    return out
