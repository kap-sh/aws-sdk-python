"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeResourcePermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.page_marker_type
    import aws_sdk_workdocs.types.principal_list


class DescribeResourcePermissionsResponse(TypedDict):
    principals: NotRequired["aws_sdk_workdocs.types.principal_list.PrincipalList"]
    """<p>The principals.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourcePermissionsResponse) -> dict:
    out: dict = {}
    if "principals" in value:
        import aws_sdk_workdocs.types.principal_list

        out["Principals"] = aws_sdk_workdocs.types.principal_list.serialize_json(
            value["principals"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeResourcePermissionsResponse:
    out: DescribeResourcePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Principals" in data:
        import aws_sdk_workdocs.types.principal_list

        out["principals"] = aws_sdk_workdocs.types.principal_list.deserialize_json(
            data["Principals"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
