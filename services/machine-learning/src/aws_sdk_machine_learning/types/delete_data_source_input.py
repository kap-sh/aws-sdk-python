"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.entity_id


class DeleteDataSourceInput(TypedDict, closed=True):
    data_source_id: "aws_sdk_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>DataSource</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataSourceInput) -> dict:
    out: dict = {}
    out["DataSourceId"] = value["data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataSourceInput:
    out: DeleteDataSourceInput = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    else:
        raise DeserializationError("DeleteDataSourceInput.data_source_id required")
    return out
