"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceGroup``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id
    import aws_sdk_kendra.types.principal_name


class DataSourceGroup(TypedDict):
    group_id: "aws_sdk_kendra.types.principal_name.PrincipalName"
    """<p>The identifier of the group you want to add to your list of groups. This is for filtering search results based on the groups' access to documents.</p>"""
    data_source_id: "aws_sdk_kendra.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source group you want to add to your list of data source groups. This is for filtering search results based on the groups' access to documents in that data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceGroup) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    out["DataSourceId"] = value["data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceGroup:
    out: DataSourceGroup = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DataSourceGroup.group_id required")
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError("DataSourceGroup.data_source_id required")
    return out
