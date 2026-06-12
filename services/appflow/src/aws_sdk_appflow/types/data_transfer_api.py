"""Generated from Smithy shape ``com.amazonaws.appflow#DataTransferApi``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.data_transfer_api_type
    import aws_sdk_appflow.types.data_transfer_api_type_name


class DataTransferApi(TypedDict):
    name: NotRequired[
        "aws_sdk_appflow.types.data_transfer_api_type_name.DataTransferApiTypeName"
    ]
    """<p>The name of the connector application API.</p>"""
    type: NotRequired[
        "aws_sdk_appflow.types.data_transfer_api_type.DataTransferApiType"
    ]
    """<p>You can specify one of the following types:</p> <dl> <dt>AUTOMATIC</dt> <dd> <p>The default. Optimizes a flow for datasets that fluctuate in size from small to large. For each flow run, Amazon AppFlow chooses to use the SYNC or ASYNC API type based on the amount of data that the run transfers.</p> </dd> <dt>SYNC</dt> <dd> <p>A synchronous API. This type of API optimizes a flow for small to medium-sized datasets.</p> </dd> <dt>ASYNC</dt> <dd> <p>An asynchronous API. This type of API optimizes a flow for large datasets.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTransferApi) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_appflow.types.data_transfer_api_type

        out["Type"] = aws_sdk_appflow.types.data_transfer_api_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> DataTransferApi:
    out: DataTransferApi = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_appflow.types.data_transfer_api_type

        out["type"] = aws_sdk_appflow.types.data_transfer_api_type.deserialize_json(
            data["Type"]
        )
    return out
