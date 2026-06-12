"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sfn.types.map_run_list_item

MapRunList: TypeAlias = list["aws_sdk_sfn.types.map_run_list_item.MapRunListItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapRunList) -> list:
    import aws_sdk_sfn.types.map_run_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_sfn.types.map_run_list_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> MapRunList:
    import aws_sdk_sfn.types.map_run_list_item

    out: MapRunList = []
    for item in data:
        out.append(aws_sdk_sfn.types.map_run_list_item.deserialize_aws_json_1_0(item))
    return out
