"""Generated from Smithy shape ``com.amazonaws.ssm#ParametersFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameters_filter_key
    import aws_sdk_ssm.types.parameters_filter_value_list


class ParametersFilter(TypedDict):
    key: "aws_sdk_ssm.types.parameters_filter_key.ParametersFilterKey"
    """<p>The name of the filter.</p>"""
    values: "aws_sdk_ssm.types.parameters_filter_value_list.ParametersFilterValueList"
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParametersFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.parameters_filter_key

    out["Key"] = aws_sdk_ssm.types.parameters_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import aws_sdk_ssm.types.parameters_filter_value_list

    out["Values"] = (
        aws_sdk_ssm.types.parameters_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParametersFilter:
    out: ParametersFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_ssm.types.parameters_filter_key

        out["key"] = aws_sdk_ssm.types.parameters_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        raise DeserializationError("ParametersFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.parameters_filter_value_list

        out["values"] = (
            aws_sdk_ssm.types.parameters_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ParametersFilter.values required")
    return out
