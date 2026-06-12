"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_information_filter_key
    import aws_sdk_ssm.types.instance_information_filter_value_set


class InstanceInformationFilter(TypedDict):
    key: (
        "aws_sdk_ssm.types.instance_information_filter_key.InstanceInformationFilterKey"
    )
    """<p>The name of the filter. </p>"""
    value_set: "aws_sdk_ssm.types.instance_information_filter_value_set.InstanceInformationFilterValueSet"
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformationFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.instance_information_filter_key

    out["key"] = (
        aws_sdk_ssm.types.instance_information_filter_key.serialize_aws_json_1_1(
            value["key"]
        )
    )
    import aws_sdk_ssm.types.instance_information_filter_value_set

    out["valueSet"] = (
        aws_sdk_ssm.types.instance_information_filter_value_set.serialize_aws_json_1_1(
            value["value_set"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInformationFilter:
    out: InstanceInformationFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_ssm.types.instance_information_filter_key

        out["key"] = (
            aws_sdk_ssm.types.instance_information_filter_key.deserialize_aws_json_1_1(
                data["key"]
            )
        )
    else:
        raise DeserializationError("InstanceInformationFilter.key required")
    if "valueSet" in data:
        import aws_sdk_ssm.types.instance_information_filter_value_set

        out["value_set"] = (
            aws_sdk_ssm.types.instance_information_filter_value_set.deserialize_aws_json_1_1(
                data["valueSet"]
            )
        )
    else:
        raise DeserializationError("InstanceInformationFilter.value_set required")
    return out
