"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.verbose


class GetDataSourceInput(TypedDict, closed=True):
    data_source_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>DataSource</code> at creation.</p>"""
    verbose: "aws_sdk_machine_learning.types.verbose.Verbose"
    """<p>Specifies whether the <code>GetDataSource</code> operation should return <code>DataSourceSchema</code>.</p> <p>If true, <code>DataSourceSchema</code> is returned.</p> <p>If false, <code>DataSourceSchema</code> is not returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataSourceInput) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    out["Verbose"] = value.get("verbose", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataSourceInput:
    out: GetDataSourceInput = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError("GetDataSourceInput.data_source_id required")
    if "Verbose" in data:
        out["verbose"] = data["Verbose"]
    else:
        out["verbose"] = False
    return out
