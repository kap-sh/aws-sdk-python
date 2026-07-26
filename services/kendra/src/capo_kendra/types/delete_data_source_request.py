"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.index_id


class DeleteDataSourceRequest(TypedDict, closed=True):
    id: "capo_kendra.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector you want to delete.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used with the data source connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataSourceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataSourceRequest:
    out: DeleteDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteDataSourceRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("DeleteDataSourceRequest.index_id required")
    return out
