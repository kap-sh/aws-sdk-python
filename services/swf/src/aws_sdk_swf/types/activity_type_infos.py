"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTypeInfos``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.activity_type_info_list
    import aws_sdk_swf.types.page_token


class ActivityTypeInfos(TypedDict):
    type_infos: "aws_sdk_swf.types.activity_type_info_list.ActivityTypeInfoList"
    """<p>List of activity type information.</p>"""
    next_page_token: NotRequired["aws_sdk_swf.types.page_token.PageToken"]
    """<p>If a <code>NextPageToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>nextPageToken</code>. Keep all other arguments unchanged.</p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTypeInfos) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.activity_type_info_list

    out["typeInfos"] = aws_sdk_swf.types.activity_type_info_list.serialize_aws_json_1_0(
        value["type_infos"]
    )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTypeInfos:
    out: ActivityTypeInfos = {}  # type: ignore[typeddict-item]
    if "typeInfos" in data:
        import aws_sdk_swf.types.activity_type_info_list

        out["type_infos"] = (
            aws_sdk_swf.types.activity_type_info_list.deserialize_aws_json_1_0(
                data["typeInfos"]
            )
        )
    else:
        raise DeserializationError("ActivityTypeInfos.type_infos required")
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
