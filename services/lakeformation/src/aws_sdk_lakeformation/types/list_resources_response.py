"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.resource_info_list
    import aws_sdk_lakeformation.types.token


class ListResourcesResponse(TypedDict):
    resource_info_list: NotRequired[
        "aws_sdk_lakeformation.types.resource_info_list.ResourceInfoList"
    ]
    """<p>A summary of the data lake resources.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve these resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesResponse) -> dict:
    out: dict = {}
    if "resource_info_list" in value:
        import aws_sdk_lakeformation.types.resource_info_list

        out["ResourceInfoList"] = (
            aws_sdk_lakeformation.types.resource_info_list.serialize_json(
                value["resource_info_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesResponse:
    out: ListResourcesResponse = {}  # type: ignore[typeddict-item]
    if "ResourceInfoList" in data:
        import aws_sdk_lakeformation.types.resource_info_list

        out["resource_info_list"] = (
            aws_sdk_lakeformation.types.resource_info_list.deserialize_json(
                data["ResourceInfoList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
