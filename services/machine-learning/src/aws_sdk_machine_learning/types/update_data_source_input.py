"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.entity_name


class UpdateDataSourceInput(TypedDict, closed=True):
    data_source_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>DataSource</code> during creation.</p>"""
    data_source_name: "aws_sdk_machine_learning.types.entity_name.EntityName"
    """<p>A new user-supplied name or description of the <code>DataSource</code> that will replace the current description. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataSourceInput) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    out["DataSourceName"] = value["data_source_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataSourceInput:
    out: UpdateDataSourceInput = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError("UpdateDataSourceInput.data_source_id required")
    if "DataSourceName" in data:
        out["data_source_name"] = data["DataSourceName"]
    else:
        raise DeserializationError("UpdateDataSourceInput.data_source_name required")
    return out
