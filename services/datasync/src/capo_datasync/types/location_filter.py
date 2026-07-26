"""Generated from Smithy shape ``com.amazonaws.datasync#LocationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.filter_values
    import capo_datasync.types.location_filter_name
    import capo_datasync.types.operator


class LocationFilter(TypedDict, closed=True):
    name: "capo_datasync.types.location_filter_name.LocationFilterName"
    """<p>The name of the filter being used. Each API call supports a list of filters that are available for it (for example, <code>LocationType</code> for <code>ListLocations</code>).</p>"""
    values: "capo_datasync.types.filter_values.FilterValues"
    """<p>The values that you want to filter for. For example, you might want to display only Amazon S3 locations.</p>"""
    operator: "capo_datasync.types.operator.Operator"
    """<p>The operator that is used to compare filter values (for example, <code>Equals</code> or <code>Contains</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationFilter) -> dict:
    out: dict = {}
    import capo_datasync.types.location_filter_name

    out["Name"] = capo_datasync.types.location_filter_name.serialize_aws_json_1_1(
        value["name"]
    )
    import capo_datasync.types.filter_values

    out["Values"] = capo_datasync.types.filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    import capo_datasync.types.operator

    out["Operator"] = capo_datasync.types.operator.serialize_aws_json_1_1(
        value["operator"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationFilter:
    out: LocationFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_datasync.types.location_filter_name

        out["name"] = capo_datasync.types.location_filter_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    else:
        raise DeserializationError("LocationFilter.name required")
    if "Values" in data:
        import capo_datasync.types.filter_values

        out["values"] = capo_datasync.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("LocationFilter.values required")
    if "Operator" in data:
        import capo_datasync.types.operator

        out["operator"] = capo_datasync.types.operator.deserialize_aws_json_1_1(
            data["Operator"]
        )
    else:
        raise DeserializationError("LocationFilter.operator required")
    return out
