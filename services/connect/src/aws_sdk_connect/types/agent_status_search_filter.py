"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusSearchFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.control_plane_attribute_filter


class AgentStatusSearchFilter(TypedDict):
    attribute_filter: NotRequired[
        "aws_sdk_connect.types.control_plane_attribute_filter.ControlPlaneAttributeFilter"
    ]
    """<p>An object that can be used to specify Tag conditions inside the <code>SearchFilter</code>. This accepts an <code>OR</code> of <code>AND</code> (List of List) input where: </p> <ul> <li> <p>The top level list specifies conditions that need to be applied with <code>OR</code> operator.</p> </li> <li> <p>The inner list specifies conditions that need to be applied with <code>AND</code> operator.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusSearchFilter) -> dict:
    out: dict = {}
    if "attribute_filter" in value:
        import aws_sdk_connect.types.control_plane_attribute_filter

        out["AttributeFilter"] = (
            aws_sdk_connect.types.control_plane_attribute_filter.serialize_json(
                value["attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentStatusSearchFilter:
    out: AgentStatusSearchFilter = {}  # type: ignore[typeddict-item]
    if "AttributeFilter" in data:
        import aws_sdk_connect.types.control_plane_attribute_filter

        out["attribute_filter"] = (
            aws_sdk_connect.types.control_plane_attribute_filter.deserialize_json(
                data["AttributeFilter"]
            )
        )
    return out
