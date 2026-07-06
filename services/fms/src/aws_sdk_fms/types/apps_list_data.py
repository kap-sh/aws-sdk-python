"""Generated from Smithy shape ``com.amazonaws.fms#AppsListData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.apps_list
    import aws_sdk_fms.types.list_id
    import aws_sdk_fms.types.previous_apps_list
    import aws_sdk_fms.types.resource_name
    import aws_sdk_fms.types.time_stamp
    import aws_sdk_fms.types.update_token


class AppsListData(TypedDict, closed=True):
    list_id: NotRequired["aws_sdk_fms.types.list_id.ListId"]
    """<p>The ID of the Firewall Manager applications list.</p>"""
    list_name: "aws_sdk_fms.types.resource_name.ResourceName"
    """<p>The name of the Firewall Manager applications list.</p>"""
    list_update_token: NotRequired["aws_sdk_fms.types.update_token.UpdateToken"]
    """<p>A unique identifier for each update to the list. When you update the list, the update token must match the token of the current version of the application list. You can retrieve the update token by getting the list. </p>"""
    create_time: NotRequired["aws_sdk_fms.types.time_stamp.TimeStamp"]
    """<p>The time that the Firewall Manager applications list was created.</p>"""
    last_update_time: NotRequired["aws_sdk_fms.types.time_stamp.TimeStamp"]
    """<p>The time that the Firewall Manager applications list was last updated.</p>"""
    apps_list: "aws_sdk_fms.types.apps_list.AppsList"
    """<p>An array of applications in the Firewall Manager applications list.</p>"""
    previous_apps_list: NotRequired[
        "aws_sdk_fms.types.previous_apps_list.PreviousAppsList"
    ]
    """<p>A map of previous version numbers to their corresponding <code>App</code> object arrays.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppsListData) -> dict:
    out: dict = {}
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    out["ListName"] = value["list_name"]
    if "list_update_token" in value:
        out["ListUpdateToken"] = value["list_update_token"]
    if "create_time" in value:
        import aws_sdk_fms.types.time_stamp

        out["CreateTime"] = aws_sdk_fms.types.time_stamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_fms.types.time_stamp

        out["LastUpdateTime"] = aws_sdk_fms.types.time_stamp.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    import aws_sdk_fms.types.apps_list

    out["AppsList"] = aws_sdk_fms.types.apps_list.serialize_aws_json_1_1(
        value["apps_list"]
    )
    if "previous_apps_list" in value:
        import aws_sdk_fms.types.previous_apps_list

        out["PreviousAppsList"] = (
            aws_sdk_fms.types.previous_apps_list.serialize_aws_json_1_1(
                value["previous_apps_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppsListData:
    out: AppsListData = {}  # type: ignore[typeddict-item]
    if "ListId" in data:
        out["list_id"] = data["ListId"]
    if "ListName" in data:
        out["list_name"] = data["ListName"]
    else:
        raise DeserializationError("AppsListData.list_name required")
    if "ListUpdateToken" in data:
        out["list_update_token"] = data["ListUpdateToken"]
    if "CreateTime" in data:
        import aws_sdk_fms.types.time_stamp

        out["create_time"] = aws_sdk_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if "LastUpdateTime" in data:
        import aws_sdk_fms.types.time_stamp

        out["last_update_time"] = aws_sdk_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["LastUpdateTime"]
        )
    if "AppsList" in data:
        import aws_sdk_fms.types.apps_list

        out["apps_list"] = aws_sdk_fms.types.apps_list.deserialize_aws_json_1_1(
            data["AppsList"]
        )
    else:
        raise DeserializationError("AppsListData.apps_list required")
    if "PreviousAppsList" in data:
        import aws_sdk_fms.types.previous_apps_list

        out["previous_apps_list"] = (
            aws_sdk_fms.types.previous_apps_list.deserialize_aws_json_1_1(
                data["PreviousAppsList"]
            )
        )
    return out
