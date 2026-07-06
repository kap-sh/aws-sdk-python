"""Generated from Smithy shape ``com.amazonaws.fms#PutAppsListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.apps_list_data
    import aws_sdk_fms.types.tag_list


class PutAppsListRequest(TypedDict, closed=True):
    apps_list: "aws_sdk_fms.types.apps_list_data.AppsListData"
    """<p>The details of the Firewall Manager applications list to be created.</p>"""
    tag_list: NotRequired["aws_sdk_fms.types.tag_list.TagList"]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAppsListRequest) -> dict:
    out: dict = {}
    import aws_sdk_fms.types.apps_list_data

    out["AppsList"] = aws_sdk_fms.types.apps_list_data.serialize_aws_json_1_1(
        value["apps_list"]
    )
    if "tag_list" in value:
        import aws_sdk_fms.types.tag_list

        out["TagList"] = aws_sdk_fms.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAppsListRequest:
    out: PutAppsListRequest = {}  # type: ignore[typeddict-item]
    if "AppsList" in data:
        import aws_sdk_fms.types.apps_list_data

        out["apps_list"] = aws_sdk_fms.types.apps_list_data.deserialize_aws_json_1_1(
            data["AppsList"]
        )
    else:
        raise DeserializationError("PutAppsListRequest.apps_list required")
    if "TagList" in data:
        import aws_sdk_fms.types.tag_list

        out["tag_list"] = aws_sdk_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
