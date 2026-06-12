"""Generated from Smithy shape ``com.amazonaws.kendra#MemberGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id
    import aws_sdk_kendra.types.group_id


class MemberGroup(TypedDict):
    group_id: "aws_sdk_kendra.types.group_id.GroupId"
    """<p>The identifier of the sub group you want to map to a group.</p>"""
    data_source_id: NotRequired["aws_sdk_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source for the sub group you want to map to a group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberGroup) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MemberGroup:
    out: MemberGroup = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("MemberGroup.group_id required")
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    return out
