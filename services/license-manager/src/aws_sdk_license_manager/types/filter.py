"""Generated from Smithy shape ``com.amazonaws.licensemanager#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.filter_name
    import aws_sdk_license_manager.types.filter_values


class Filter(TypedDict):
    name: NotRequired["aws_sdk_license_manager.types.filter_name.FilterName"]
    """<p>Name of the filter. Filter names are case-sensitive.</p>"""
    values: NotRequired["aws_sdk_license_manager.types.filter_values.FilterValues"]
    """<p>The value of the filter, which is case-sensitive. You can only specify one value for the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_license_manager.types.filter_values

        out["Values"] = (
            aws_sdk_license_manager.types.filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_license_manager.types.filter_values

        out["values"] = (
            aws_sdk_license_manager.types.filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
