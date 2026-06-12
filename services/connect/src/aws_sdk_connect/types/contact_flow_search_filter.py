"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSearchFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_attribute_filter
    import aws_sdk_connect.types.control_plane_tag_filter


class ContactFlowSearchFilter(TypedDict):
    tag_filter: NotRequired[
        "aws_sdk_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]
    flow_attribute_filter: NotRequired[
        "aws_sdk_connect.types.contact_flow_attribute_filter.ContactFlowAttributeFilter"
    ]
    """<p> Flow attribute filter for contact flow search operations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSearchFilter) -> dict:
    out: dict = {}
    if "tag_filter" in value:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["TagFilter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.serialize_json(
                value["tag_filter"]
            )
        )
    if "flow_attribute_filter" in value:
        import aws_sdk_connect.types.contact_flow_attribute_filter

        out["FlowAttributeFilter"] = (
            aws_sdk_connect.types.contact_flow_attribute_filter.serialize_json(
                value["flow_attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowSearchFilter:
    out: ContactFlowSearchFilter = {}  # type: ignore[typeddict-item]
    if "TagFilter" in data:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["tag_filter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.deserialize_json(
                data["TagFilter"]
            )
        )
    if "FlowAttributeFilter" in data:
        import aws_sdk_connect.types.contact_flow_attribute_filter

        out["flow_attribute_filter"] = (
            aws_sdk_connect.types.contact_flow_attribute_filter.deserialize_json(
                data["FlowAttributeFilter"]
            )
        )
    return out
