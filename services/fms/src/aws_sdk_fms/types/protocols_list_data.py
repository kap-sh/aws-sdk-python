"""Generated from Smithy shape ``com.amazonaws.fms#ProtocolsListData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.list_id
    import aws_sdk_fms.types.previous_protocols_list
    import aws_sdk_fms.types.protocols_list
    import aws_sdk_fms.types.resource_name
    import aws_sdk_fms.types.time_stamp
    import aws_sdk_fms.types.update_token


class ProtocolsListData(TypedDict):
    list_id: NotRequired["aws_sdk_fms.types.list_id.ListId"]
    """<p>The ID of the Firewall Manager protocols list.</p>"""
    list_name: "aws_sdk_fms.types.resource_name.ResourceName"
    """<p>The name of the Firewall Manager protocols list.</p>"""
    list_update_token: NotRequired["aws_sdk_fms.types.update_token.UpdateToken"]
    """<p>A unique identifier for each update to the list. When you update the list, the update token must match the token of the current version of the application list. You can retrieve the update token by getting the list. </p>"""
    create_time: NotRequired["aws_sdk_fms.types.time_stamp.TimeStamp"]
    """<p>The time that the Firewall Manager protocols list was created.</p>"""
    last_update_time: NotRequired["aws_sdk_fms.types.time_stamp.TimeStamp"]
    """<p>The time that the Firewall Manager protocols list was last updated.</p>"""
    protocols_list: "aws_sdk_fms.types.protocols_list.ProtocolsList"
    """<p>An array of protocols in the Firewall Manager protocols list.</p>"""
    previous_protocols_list: NotRequired[
        "aws_sdk_fms.types.previous_protocols_list.PreviousProtocolsList"
    ]
    """<p>A map of previous version numbers to their corresponding protocol arrays.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolsListData) -> dict:
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
    import aws_sdk_fms.types.protocols_list

    out["ProtocolsList"] = aws_sdk_fms.types.protocols_list.serialize_aws_json_1_1(
        value["protocols_list"]
    )
    if "previous_protocols_list" in value:
        import aws_sdk_fms.types.previous_protocols_list

        out["PreviousProtocolsList"] = (
            aws_sdk_fms.types.previous_protocols_list.serialize_aws_json_1_1(
                value["previous_protocols_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtocolsListData:
    out: ProtocolsListData = {}  # type: ignore[typeddict-item]
    if "ListId" in data:
        out["list_id"] = data["ListId"]
    if "ListName" in data:
        out["list_name"] = data["ListName"]
    else:
        raise DeserializationError("ProtocolsListData.list_name required")
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
    if "ProtocolsList" in data:
        import aws_sdk_fms.types.protocols_list

        out["protocols_list"] = (
            aws_sdk_fms.types.protocols_list.deserialize_aws_json_1_1(
                data["ProtocolsList"]
            )
        )
    else:
        raise DeserializationError("ProtocolsListData.protocols_list required")
    if "PreviousProtocolsList" in data:
        import aws_sdk_fms.types.previous_protocols_list

        out["previous_protocols_list"] = (
            aws_sdk_fms.types.previous_protocols_list.deserialize_aws_json_1_1(
                data["PreviousProtocolsList"]
            )
        )
    return out
