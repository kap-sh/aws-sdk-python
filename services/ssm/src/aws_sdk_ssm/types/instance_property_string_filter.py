"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_property_filter_operator
    import aws_sdk_ssm.types.instance_property_filter_value_set
    import aws_sdk_ssm.types.instance_property_string_filter_key


class InstancePropertyStringFilter(TypedDict, closed=True):
    key: "aws_sdk_ssm.types.instance_property_string_filter_key.InstancePropertyStringFilterKey"
    """<p>The filter key name to describe your managed nodes.</p>"""
    values: "aws_sdk_ssm.types.instance_property_filter_value_set.InstancePropertyFilterValueSet"
    """<p>The filter key name to describe your managed nodes.</p>"""
    operator: NotRequired[
        "aws_sdk_ssm.types.instance_property_filter_operator.InstancePropertyFilterOperator"
    ]
    """<p>The operator used by the filter call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyStringFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_ssm.types.instance_property_filter_value_set

    out["Values"] = (
        aws_sdk_ssm.types.instance_property_filter_value_set.serialize_aws_json_1_1(
            value["values"]
        )
    )
    if "operator" in value:
        import aws_sdk_ssm.types.instance_property_filter_operator

        out["Operator"] = (
            aws_sdk_ssm.types.instance_property_filter_operator.serialize_aws_json_1_1(
                value["operator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePropertyStringFilter:
    out: InstancePropertyStringFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("InstancePropertyStringFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.instance_property_filter_value_set

        out["values"] = (
            aws_sdk_ssm.types.instance_property_filter_value_set.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("InstancePropertyStringFilter.values required")
    if "Operator" in data:
        import aws_sdk_ssm.types.instance_property_filter_operator

        out["operator"] = (
            aws_sdk_ssm.types.instance_property_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    return out
