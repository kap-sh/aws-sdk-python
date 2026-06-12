"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_filter_key
    import aws_sdk_ssm.types.ops_item_filter_operator
    import aws_sdk_ssm.types.ops_item_filter_values


class OpsItemFilter(TypedDict):
    key: "aws_sdk_ssm.types.ops_item_filter_key.OpsItemFilterKey"
    """<p>The name of the filter.</p>"""
    values: "aws_sdk_ssm.types.ops_item_filter_values.OpsItemFilterValues"
    """<p>The filter value.</p>"""
    operator: "aws_sdk_ssm.types.ops_item_filter_operator.OpsItemFilterOperator"
    """<p>The operator used by the filter call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.ops_item_filter_key

    out["Key"] = aws_sdk_ssm.types.ops_item_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import aws_sdk_ssm.types.ops_item_filter_values

    out["Values"] = aws_sdk_ssm.types.ops_item_filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    import aws_sdk_ssm.types.ops_item_filter_operator

    out["Operator"] = aws_sdk_ssm.types.ops_item_filter_operator.serialize_aws_json_1_1(
        value["operator"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemFilter:
    out: OpsItemFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_ssm.types.ops_item_filter_key

        out["key"] = aws_sdk_ssm.types.ops_item_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        raise DeserializationError("OpsItemFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.ops_item_filter_values

        out["values"] = (
            aws_sdk_ssm.types.ops_item_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("OpsItemFilter.values required")
    if "Operator" in data:
        import aws_sdk_ssm.types.ops_item_filter_operator

        out["operator"] = (
            aws_sdk_ssm.types.ops_item_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("OpsItemFilter.operator required")
    return out
