"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateDataSourceFromRDSOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class CreateDataSourceFromRDSOutput(TypedDict):
    data_source_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>A user-supplied ID that uniquely identifies the datasource. This value should be identical to the value of the <code>DataSourceID</code> in the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceFromRDSOutput) -> dict:
    out: dict = {}
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceFromRDSOutput:
    out: CreateDataSourceFromRDSOutput = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    return out
