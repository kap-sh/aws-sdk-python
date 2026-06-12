"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.data_source_arn
    import aws_sdk_qbusiness.types.data_source_id

class CreateDataSourceResponse(TypedDict):
    data_source_id: NotRequired["aws_sdk_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source connector.</p>"""
    data_source_arn: NotRequired["aws_sdk_qbusiness.types.data_source_arn.DataSourceArn"]
    """<p> The Amazon Resource Name (ARN) of a data source in an Amazon Q Business application. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    if "data_source_arn" in value:
        out["dataSourceArn"] = value["data_source_arn"]
    return out


def deserialize_json(data: dict) -> CreateDataSourceResponse:
    out: CreateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "dataSourceId" in data:
        out["data_source_id"] = data["dataSourceId"]
    if "dataSourceArn" in data:
        out["data_source_arn"] = data["dataSourceArn"]
    return out