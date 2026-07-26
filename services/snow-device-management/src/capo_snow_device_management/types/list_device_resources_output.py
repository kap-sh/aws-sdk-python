"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ListDeviceResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.next_token
    import capo_snow_device_management.types.resource_summary_list


class ListDeviceResourcesOutput(TypedDict, closed=True):
    resources: NotRequired[
        "capo_snow_device_management.types.resource_summary_list.ResourceSummaryList"
    ]
    """<p>A structure defining the resource's type, Amazon Resource Name (ARN), and ID.</p>"""
    next_token: NotRequired["capo_snow_device_management.types.next_token.NextToken"]
    """<p>A pagination token to continue to the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeviceResourcesOutput) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_snow_device_management.types.resource_summary_list

        out["resources"] = (
            capo_snow_device_management.types.resource_summary_list.serialize_json(
                value["resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeviceResourcesOutput:
    out: ListDeviceResourcesOutput = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import capo_snow_device_management.types.resource_summary_list

        out["resources"] = (
            capo_snow_device_management.types.resource_summary_list.deserialize_json(
                data["resources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
