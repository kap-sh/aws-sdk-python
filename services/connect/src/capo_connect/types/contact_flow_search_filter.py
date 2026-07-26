"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_attribute_filter
    import capo_connect.types.control_plane_tag_filter


class ContactFlowSearchFilter(TypedDict, closed=True):
    tag_filter: NotRequired[
        "capo_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]
    flow_attribute_filter: NotRequired[
        "capo_connect.types.contact_flow_attribute_filter.ContactFlowAttributeFilter"
    ]
    """<p> Flow attribute filter for contact flow search operations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSearchFilter) -> dict:
    out: dict = {}
    if "tag_filter" in value:
        import capo_connect.types.control_plane_tag_filter

        out["TagFilter"] = capo_connect.types.control_plane_tag_filter.serialize_json(
            value["tag_filter"]
        )
    if "flow_attribute_filter" in value:
        import capo_connect.types.contact_flow_attribute_filter

        out["FlowAttributeFilter"] = (
            capo_connect.types.contact_flow_attribute_filter.serialize_json(
                value["flow_attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowSearchFilter:
    out: ContactFlowSearchFilter = {}  # type: ignore[typeddict-item]
    if "TagFilter" in data:
        import capo_connect.types.control_plane_tag_filter

        out["tag_filter"] = (
            capo_connect.types.control_plane_tag_filter.deserialize_json(
                data["TagFilter"]
            )
        )
    if "FlowAttributeFilter" in data:
        import capo_connect.types.contact_flow_attribute_filter

        out["flow_attribute_filter"] = (
            capo_connect.types.contact_flow_attribute_filter.deserialize_json(
                data["FlowAttributeFilter"]
            )
        )
    return out
