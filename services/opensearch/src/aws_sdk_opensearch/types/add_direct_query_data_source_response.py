"""Generated from Smithy shape ``com.amazonaws.opensearch#AddDirectQueryDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.string


class AddDirectQueryDataSourceResponse(TypedDict):
    data_source_arn: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p> The unique, system-generated identifier that represents the data source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDirectQueryDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source_arn" in value:
        out["DataSourceArn"] = value["data_source_arn"]
    return out


def deserialize_json(data: dict) -> AddDirectQueryDataSourceResponse:
    out: AddDirectQueryDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    return out
