"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.group_name
    import aws_sdk_qbusiness.types.index_id


class GetGroupRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application id the group is attached to.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index the group is attached to.</p>"""
    group_name: "aws_sdk_qbusiness.types.group_name.GroupName"
    """<p>The name of the group.</p>"""
    data_source_id: NotRequired["aws_sdk_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source the group is attached to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGroupRequest:
    out: GetGroupRequest = {}  # type: ignore[typeddict-item]
    return out
