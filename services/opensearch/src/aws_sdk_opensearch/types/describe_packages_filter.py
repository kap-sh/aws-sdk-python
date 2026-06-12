"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribePackagesFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.describe_packages_filter_name
    import aws_sdk_opensearch.types.describe_packages_filter_values


class DescribePackagesFilter(TypedDict):
    name: NotRequired[
        "aws_sdk_opensearch.types.describe_packages_filter_name.DescribePackagesFilterName"
    ]
    """<p>Any field from <code>PackageDetails</code>.</p>"""
    value: NotRequired[
        "aws_sdk_opensearch.types.describe_packages_filter_values.DescribePackagesFilterValues"
    ]
    """<p>A non-empty list of values for the specified filter field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_opensearch.types.describe_packages_filter_name

        out["Name"] = (
            aws_sdk_opensearch.types.describe_packages_filter_name.serialize_json(
                value["name"]
            )
        )
    if "value" in value:
        import aws_sdk_opensearch.types.describe_packages_filter_values

        out["Value"] = (
            aws_sdk_opensearch.types.describe_packages_filter_values.serialize_json(
                value["value"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribePackagesFilter:
    out: DescribePackagesFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_opensearch.types.describe_packages_filter_name

        out["name"] = (
            aws_sdk_opensearch.types.describe_packages_filter_name.deserialize_json(
                data["Name"]
            )
        )
    if "Value" in data:
        import aws_sdk_opensearch.types.describe_packages_filter_values

        out["value"] = (
            aws_sdk_opensearch.types.describe_packages_filter_values.deserialize_json(
                data["Value"]
            )
        )
    return out
