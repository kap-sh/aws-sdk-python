"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.instance_property_filter_operator
    import capo_ssm.types.instance_property_filter_value_set
    import capo_ssm.types.instance_property_string_filter_key


class InstancePropertyStringFilter(TypedDict, closed=True):
    key: "capo_ssm.types.instance_property_string_filter_key.InstancePropertyStringFilterKey"
    """<p>The filter key name to describe your managed nodes.</p>"""
    values: "capo_ssm.types.instance_property_filter_value_set.InstancePropertyFilterValueSet"
    """<p>The filter key name to describe your managed nodes.</p>"""
    operator: NotRequired[
        "capo_ssm.types.instance_property_filter_operator.InstancePropertyFilterOperator"
    ]
    """<p>The operator used by the filter call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyStringFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_ssm.types.instance_property_filter_value_set

    out["Values"] = (
        capo_ssm.types.instance_property_filter_value_set.serialize_aws_json_1_1(
            value["values"]
        )
    )
    if "operator" in value:
        import capo_ssm.types.instance_property_filter_operator

        out["Operator"] = (
            capo_ssm.types.instance_property_filter_operator.serialize_aws_json_1_1(
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
        import capo_ssm.types.instance_property_filter_value_set

        out["values"] = (
            capo_ssm.types.instance_property_filter_value_set.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("InstancePropertyStringFilter.values required")
    if "Operator" in data:
        import capo_ssm.types.instance_property_filter_operator

        out["operator"] = (
            capo_ssm.types.instance_property_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    return out
