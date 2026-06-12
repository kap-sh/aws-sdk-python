"""Generated from Smithy shape ``com.amazonaws.appstream#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.filter_name
    import aws_sdk_appstream.types.filter_values


class Filter(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.filter_name.FilterName"]
    """<p>The name of the filter. Valid filter names depend on the operation being performed.</p>"""
    values: NotRequired["aws_sdk_appstream.types.filter_values.FilterValues"]
    """<p>The values for the filter. Multiple values can be specified for a single filter name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_appstream.types.filter_values

        out["Values"] = aws_sdk_appstream.types.filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_appstream.types.filter_values

        out["values"] = aws_sdk_appstream.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
