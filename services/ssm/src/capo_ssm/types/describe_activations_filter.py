"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeActivationsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.describe_activations_filter_keys
    import capo_ssm.types.string_list


class DescribeActivationsFilter(TypedDict, closed=True):
    filter_key: NotRequired[
        "capo_ssm.types.describe_activations_filter_keys.DescribeActivationsFilterKeys"
    ]
    """<p>The name of the filter.</p>"""
    filter_values: NotRequired["capo_ssm.types.string_list.StringList"]
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeActivationsFilter) -> dict:
    out: dict = {}
    if "filter_key" in value:
        import capo_ssm.types.describe_activations_filter_keys

        out["FilterKey"] = (
            capo_ssm.types.describe_activations_filter_keys.serialize_aws_json_1_1(
                value["filter_key"]
            )
        )
    if "filter_values" in value:
        import capo_ssm.types.string_list

        out["FilterValues"] = capo_ssm.types.string_list.serialize_aws_json_1_1(
            value["filter_values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeActivationsFilter:
    out: DescribeActivationsFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterKey") is not None:
        import capo_ssm.types.describe_activations_filter_keys

        out["filter_key"] = (
            capo_ssm.types.describe_activations_filter_keys.deserialize_aws_json_1_1(
                data["FilterKey"]
            )
        )
    if data.get("FilterValues") is not None:
        import capo_ssm.types.string_list

        out["filter_values"] = capo_ssm.types.string_list.deserialize_aws_json_1_1(
            data["FilterValues"]
        )
    return out
