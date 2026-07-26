"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.volume_filter_name
    import capo_fsx.types.volume_filter_values


class VolumeFilter(TypedDict, closed=True):
    name: NotRequired["capo_fsx.types.volume_filter_name.VolumeFilterName"]
    """<p>The name for this filter.</p>"""
    values: NotRequired["capo_fsx.types.volume_filter_values.VolumeFilterValues"]
    """<p>The values of the filter. These are all the values for any of the applied filters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_fsx.types.volume_filter_name

        out["Name"] = capo_fsx.types.volume_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "values" in value:
        import capo_fsx.types.volume_filter_values

        out["Values"] = capo_fsx.types.volume_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VolumeFilter:
    out: VolumeFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_fsx.types.volume_filter_name

        out["name"] = capo_fsx.types.volume_filter_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    if "Values" in data:
        import capo_fsx.types.volume_filter_values

        out["values"] = capo_fsx.types.volume_filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
