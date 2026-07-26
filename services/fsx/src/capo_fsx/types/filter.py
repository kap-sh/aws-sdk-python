"""Generated from Smithy shape ``com.amazonaws.fsx#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.filter_name
    import capo_fsx.types.filter_values


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_fsx.types.filter_name.FilterName"]
    """<p>The name for this filter.</p>"""
    values: NotRequired["capo_fsx.types.filter_values.FilterValues"]
    """<p>The values of the filter. These are all the values for any of the applied filters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_fsx.types.filter_name

        out["Name"] = capo_fsx.types.filter_name.serialize_aws_json_1_1(value["name"])
    if "values" in value:
        import capo_fsx.types.filter_values

        out["Values"] = capo_fsx.types.filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_fsx.types.filter_name

        out["name"] = capo_fsx.types.filter_name.deserialize_aws_json_1_1(data["Name"])
    if "Values" in data:
        import capo_fsx.types.filter_values

        out["values"] = capo_fsx.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
