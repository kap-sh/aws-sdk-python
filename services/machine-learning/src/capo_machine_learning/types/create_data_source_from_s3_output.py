"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateDataSourceFromS3Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class CreateDataSourceFromS3Output(TypedDict, closed=True):
    data_source_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>A user-supplied ID that uniquely identifies the <code>DataSource</code>. This value should be identical to the value of the <code>DataSourceID</code> in the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataSourceFromS3Output) -> dict:
    out: dict = {}
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataSourceFromS3Output:
    out: CreateDataSourceFromS3Output = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    return out
