"""Generated from Smithy shape ``com.amazonaws.connect#DeleteDataTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.instance_id


class DeleteDataTableRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table to delete. Must also accept the table ARN. Fails with an error if the version is provided and is not $LATEST.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataTableRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataTableRequest:
    out: DeleteDataTableRequest = {}  # type: ignore[typeddict-item]
    return out
