"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.step_execution_filter_key
    import capo_ssm.types.step_execution_filter_value_list


class StepExecutionFilter(TypedDict, closed=True):
    key: "capo_ssm.types.step_execution_filter_key.StepExecutionFilterKey"
    """<p>One or more keys to limit the results.</p>"""
    values: (
        "capo_ssm.types.step_execution_filter_value_list.StepExecutionFilterValueList"
    )
    """<p>The values of the filter key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.step_execution_filter_key

    out["Key"] = capo_ssm.types.step_execution_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import capo_ssm.types.step_execution_filter_value_list

    out["Values"] = (
        capo_ssm.types.step_execution_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepExecutionFilter:
    out: StepExecutionFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import capo_ssm.types.step_execution_filter_key

        out["key"] = capo_ssm.types.step_execution_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        raise DeserializationError("StepExecutionFilter.key required")
    if "Values" in data:
        import capo_ssm.types.step_execution_filter_value_list

        out["values"] = (
            capo_ssm.types.step_execution_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("StepExecutionFilter.values required")
    return out
