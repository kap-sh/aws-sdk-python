"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.step_execution_filter_key
    import aws_sdk_ssm.types.step_execution_filter_value_list


class StepExecutionFilter(TypedDict, closed=True):
    key: "aws_sdk_ssm.types.step_execution_filter_key.StepExecutionFilterKey"
    """<p>One or more keys to limit the results.</p>"""
    values: "aws_sdk_ssm.types.step_execution_filter_value_list.StepExecutionFilterValueList"
    """<p>The values of the filter key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.step_execution_filter_key

    out["Key"] = aws_sdk_ssm.types.step_execution_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import aws_sdk_ssm.types.step_execution_filter_value_list

    out["Values"] = (
        aws_sdk_ssm.types.step_execution_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepExecutionFilter:
    out: StepExecutionFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_ssm.types.step_execution_filter_key

        out["key"] = (
            aws_sdk_ssm.types.step_execution_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    else:
        raise DeserializationError("StepExecutionFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.step_execution_filter_value_list

        out["values"] = (
            aws_sdk_ssm.types.step_execution_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("StepExecutionFilter.values required")
    return out
