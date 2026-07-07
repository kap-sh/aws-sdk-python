"""Generated from Smithy shape ``com.amazonaws.qbusiness#UserAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.string


class UserAlias(TypedDict, closed=True):
    index_id: NotRequired["aws_sdk_qbusiness.types.index_id.IndexId"]
    """<p>The identifier of the index that the user aliases are associated with.</p>"""
    data_source_id: NotRequired["aws_sdk_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source that the user aliases are associated with.</p>"""
    user_id: "aws_sdk_qbusiness.types.string.String"
    """<p>The identifier of the user id associated with the user aliases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAlias) -> dict:
    out: dict = {}
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UserAlias:
    out: UserAlias = {}  # type: ignore[typeddict-item]
    if "indexId" in data:
        out["index_id"] = data["indexId"]
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UserAlias.user_id required")
    return out
