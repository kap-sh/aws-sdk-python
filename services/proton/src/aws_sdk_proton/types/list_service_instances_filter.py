"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceInstancesFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.list_service_instances_filter_by
    import aws_sdk_proton.types.list_service_instances_filter_value


class ListServiceInstancesFilter(TypedDict):
    key: NotRequired[
        "aws_sdk_proton.types.list_service_instances_filter_by.ListServiceInstancesFilterBy"
    ]
    """<p>The name of a filtering criterion.</p>"""
    value: NotRequired[
        "aws_sdk_proton.types.list_service_instances_filter_value.ListServiceInstancesFilterValue"
    ]
    """<p>A value to filter by.</p> <p>With the date/time keys (<code>*At{Before,After}</code>), the value is a valid <a href=\"https://datatracker.ietf.org/doc/html/rfc3339.html\">RFC 3339</a> string with no UTC offset and with an optional fractional precision (for example, <code>1985-04-12T23:20:50.52Z</code>).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceInstancesFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceInstancesFilter:
    out: ListServiceInstancesFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
