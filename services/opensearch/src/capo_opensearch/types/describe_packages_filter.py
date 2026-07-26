"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribePackagesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.describe_packages_filter_name
    import capo_opensearch.types.describe_packages_filter_values


class DescribePackagesFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_opensearch.types.describe_packages_filter_name.DescribePackagesFilterName"
    ]
    """<p>Any field from <code>PackageDetails</code>.</p>"""
    value: NotRequired[
        "capo_opensearch.types.describe_packages_filter_values.DescribePackagesFilterValues"
    ]
    """<p>A non-empty list of values for the specified filter field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_opensearch.types.describe_packages_filter_name

        out["Name"] = (
            capo_opensearch.types.describe_packages_filter_name.serialize_json(
                value["name"]
            )
        )
    if "value" in value:
        import capo_opensearch.types.describe_packages_filter_values

        out["Value"] = (
            capo_opensearch.types.describe_packages_filter_values.serialize_json(
                value["value"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribePackagesFilter:
    out: DescribePackagesFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_opensearch.types.describe_packages_filter_name

        out["name"] = (
            capo_opensearch.types.describe_packages_filter_name.deserialize_json(
                data["Name"]
            )
        )
    if "Value" in data:
        import capo_opensearch.types.describe_packages_filter_values

        out["value"] = (
            capo_opensearch.types.describe_packages_filter_values.deserialize_json(
                data["Value"]
            )
        )
    return out
