"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.control_plane_tag_filter


class TestCaseSearchFilter(TypedDict, closed=True):
    tag_filter: NotRequired[
        "aws_sdk_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]
    """<p>An object that can be used to specify Tag conditions inside the SearchFilter. This accepts an OR of AND (List of List) input where: Top level list specifies conditions that need to be applied with OR operator. Inner list specifies conditions that need to be applied with AND operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseSearchFilter) -> dict:
    out: dict = {}
    if "tag_filter" in value:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["TagFilter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.serialize_json(
                value["tag_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestCaseSearchFilter:
    out: TestCaseSearchFilter = {}  # type: ignore[typeddict-item]
    if "TagFilter" in data:
        import aws_sdk_connect.types.control_plane_tag_filter

        out["tag_filter"] = (
            aws_sdk_connect.types.control_plane_tag_filter.deserialize_json(
                data["TagFilter"]
            )
        )
    return out
