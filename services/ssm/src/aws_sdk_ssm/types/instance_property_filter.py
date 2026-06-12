"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_property_filter_key
    import aws_sdk_ssm.types.instance_property_filter_value_set


class InstancePropertyFilter(TypedDict):
    key: "aws_sdk_ssm.types.instance_property_filter_key.InstancePropertyFilterKey"
    """<p>The name of the filter.</p>"""
    value_set: "aws_sdk_ssm.types.instance_property_filter_value_set.InstancePropertyFilterValueSet"
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.instance_property_filter_key

    out["key"] = aws_sdk_ssm.types.instance_property_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import aws_sdk_ssm.types.instance_property_filter_value_set

    out["valueSet"] = (
        aws_sdk_ssm.types.instance_property_filter_value_set.serialize_aws_json_1_1(
            value["value_set"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePropertyFilter:
    out: InstancePropertyFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_ssm.types.instance_property_filter_key

        out["key"] = (
            aws_sdk_ssm.types.instance_property_filter_key.deserialize_aws_json_1_1(
                data["key"]
            )
        )
    else:
        raise DeserializationError("InstancePropertyFilter.key required")
    if "valueSet" in data:
        import aws_sdk_ssm.types.instance_property_filter_value_set

        out["value_set"] = (
            aws_sdk_ssm.types.instance_property_filter_value_set.deserialize_aws_json_1_1(
                data["valueSet"]
            )
        )
    else:
        raise DeserializationError("InstancePropertyFilter.value_set required")
    return out
