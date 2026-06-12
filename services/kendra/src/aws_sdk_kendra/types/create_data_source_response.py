"""Generated from Smithy shape ``com.amazonaws.kendra#CreateDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id


class CreateDataSourceResponse(TypedDict):
    id: "aws_sdk_kendra.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceResponse:
    out: CreateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CreateDataSourceResponse.id required")
    return out
