"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListCommonControlsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.common_control_summary_list
    import aws_sdk_controlcatalog.types.pagination_token


class ListCommonControlsResponse(TypedDict):
    common_controls: "aws_sdk_controlcatalog.types.common_control_summary_list.CommonControlSummaryList"
    """<p>The list of common controls that the <code>ListCommonControls</code> API returns.</p>"""
    next_token: NotRequired[
        "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommonControlsResponse) -> dict:
    out: dict = {}
    import aws_sdk_controlcatalog.types.common_control_summary_list

    out["CommonControls"] = (
        aws_sdk_controlcatalog.types.common_control_summary_list.serialize_json(
            value["common_controls"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCommonControlsResponse:
    out: ListCommonControlsResponse = {}  # type: ignore[typeddict-item]
    if "CommonControls" in data:
        import aws_sdk_controlcatalog.types.common_control_summary_list

        out["common_controls"] = (
            aws_sdk_controlcatalog.types.common_control_summary_list.deserialize_json(
                data["CommonControls"]
            )
        )
    else:
        raise DeserializationError(
            "ListCommonControlsResponse.common_controls required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
