"""Generated from Smithy shape ``com.amazonaws.connect#UserSearchFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.control_plane_tag_filter
    import aws_sdk_connect.types.control_plane_user_attribute_filter


class UserSearchFilter(TypedDict):
    tag_filter: NotRequired[
        "aws_sdk_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]
    user_attribute_filter: NotRequired[
        "aws_sdk_connect.types.control_plane_user_attribute_filter.ControlPlaneUserAttributeFilter"
    ]
    """<p>An object that can be used to specify Tag conditions or Hierarchy Group conditions inside the SearchFilter.</p> <p>This accepts an <code>OR</code> of <code>AND</code> (List of List) input where:</p> <ul> <li> <p>The top level list specifies conditions that need to be applied with <code>OR</code> operator.</p> </li> <li> <p>The inner list specifies conditions that need to be applied with <code>AND</code> operator.</p> </li> </ul> <note> <p>Only one field can be populated. This object can’t be used along with TagFilter. Request can either contain TagFilter or UserAttributeFilter if SearchFilter is specified, combination of both is not supported and such request will throw AccessDeniedException.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSearchFilter) -> dict:
    out: dict = {}
    if "tag_filter" in value:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["TagFilter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.serialize_json(
                value["tag_filter"]
            )
        )
    if "user_attribute_filter" in value:
        import aws_sdk_connect.types.control_plane_user_attribute_filter

        out["UserAttributeFilter"] = (
            aws_sdk_connect.types.control_plane_user_attribute_filter.serialize_json(
                value["user_attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserSearchFilter:
    out: UserSearchFilter = {}  # type: ignore[typeddict-item]
    if "TagFilter" in data:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["tag_filter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.deserialize_json(
                data["TagFilter"]
            )
        )
    if "UserAttributeFilter" in data:
        import aws_sdk_connect.types.control_plane_user_attribute_filter

        out["user_attribute_filter"] = (
            aws_sdk_connect.types.control_plane_user_attribute_filter.deserialize_json(
                data["UserAttributeFilter"]
            )
        )
    return out
