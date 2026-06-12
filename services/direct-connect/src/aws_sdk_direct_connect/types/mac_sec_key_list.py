"""Generated from Smithy shape ``com.amazonaws.directconnect#MacSecKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.mac_sec_key

MacSecKeyList: TypeAlias = list["aws_sdk_direct_connect.types.mac_sec_key.MacSecKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MacSecKeyList) -> list:
    import aws_sdk_direct_connect.types.mac_sec_key

    out: list = []
    for item in value:
        out.append(
            aws_sdk_direct_connect.types.mac_sec_key.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MacSecKeyList:
    import aws_sdk_direct_connect.types.mac_sec_key

    out: MacSecKeyList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.mac_sec_key.deserialize_aws_json_1_1(item)
        )
    return out
