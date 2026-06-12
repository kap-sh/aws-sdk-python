"""Generated from Smithy shape ``com.amazonaws.finspacedata#CreateDataViewRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.boolean
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.data_view_destination_type_params
    import aws_sdk_finspace_data.types.dataset_id
    import aws_sdk_finspace_data.types.partition_column_list
    import aws_sdk_finspace_data.types.sort_column_list
    import aws_sdk_finspace_data.types.timestamp_epoch


class CreateDataViewRequest(TypedDict):
    client_token: NotRequired["aws_sdk_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    dataset_id: "aws_sdk_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique Dataset identifier that is used to create a Dataview.</p>"""
    auto_update: "aws_sdk_finspace_data.types.boolean.Boolean"
    """<p>Flag to indicate Dataview should be updated automatically.</p>"""
    sort_columns: NotRequired[
        "aws_sdk_finspace_data.types.sort_column_list.SortColumnList"
    ]
    """<p>Columns to be used for sorting the data.</p>"""
    partition_columns: NotRequired[
        "aws_sdk_finspace_data.types.partition_column_list.PartitionColumnList"
    ]
    """<p>Ordered set of column names used to partition data.</p>"""
    as_of_timestamp: NotRequired[
        "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    ]
    """<p>Beginning time to use for the Dataview. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    destination_type_params: "aws_sdk_finspace_data.types.data_view_destination_type_params.DataViewDestinationTypeParams"
    """<p>Options that define the destination type for the Dataview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataViewRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["autoUpdate"] = value.get("auto_update", False)
    if "sort_columns" in value:
        import aws_sdk_finspace_data.types.sort_column_list

        out["sortColumns"] = (
            aws_sdk_finspace_data.types.sort_column_list.serialize_json(
                value["sort_columns"]
            )
        )
    if "partition_columns" in value:
        import aws_sdk_finspace_data.types.partition_column_list

        out["partitionColumns"] = (
            aws_sdk_finspace_data.types.partition_column_list.serialize_json(
                value["partition_columns"]
            )
        )
    if "as_of_timestamp" in value:
        out["asOfTimestamp"] = value["as_of_timestamp"]
    import aws_sdk_finspace_data.types.data_view_destination_type_params

    out["destinationTypeParams"] = (
        aws_sdk_finspace_data.types.data_view_destination_type_params.serialize_json(
            value["destination_type_params"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateDataViewRequest:
    out: CreateDataViewRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "autoUpdate" in data:
        out["auto_update"] = data["autoUpdate"]
    else:
        out["auto_update"] = False
    if "sortColumns" in data:
        import aws_sdk_finspace_data.types.sort_column_list

        out["sort_columns"] = (
            aws_sdk_finspace_data.types.sort_column_list.deserialize_json(
                data["sortColumns"]
            )
        )
    if "partitionColumns" in data:
        import aws_sdk_finspace_data.types.partition_column_list

        out["partition_columns"] = (
            aws_sdk_finspace_data.types.partition_column_list.deserialize_json(
                data["partitionColumns"]
            )
        )
    if "asOfTimestamp" in data:
        out["as_of_timestamp"] = data["asOfTimestamp"]
    if "destinationTypeParams" in data:
        import aws_sdk_finspace_data.types.data_view_destination_type_params

        out["destination_type_params"] = (
            aws_sdk_finspace_data.types.data_view_destination_type_params.deserialize_json(
                data["destinationTypeParams"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataViewRequest.destination_type_params required"
        )
    return out
