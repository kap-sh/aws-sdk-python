"""Generated from Smithy shape ``com.amazonaws.ram#ListResourceTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.service_name_and_resource_type_list
    import capo_ram.types.string


class ListResourceTypesResponse(TypedDict, closed=True):
    resource_types: NotRequired[
        "capo_ram.types.service_name_and_resource_type_list.ServiceNameAndResourceTypeList"
    ]
    """<p>An array of objects that contain information about the resource types that can be shared using RAM.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceTypesResponse) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import capo_ram.types.service_name_and_resource_type_list

        out["resourceTypes"] = (
            capo_ram.types.service_name_and_resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceTypesResponse:
    out: ListResourceTypesResponse = {}  # type: ignore[typeddict-item]
    if "resourceTypes" in data:
        import capo_ram.types.service_name_and_resource_type_list

        out["resource_types"] = (
            capo_ram.types.service_name_and_resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
