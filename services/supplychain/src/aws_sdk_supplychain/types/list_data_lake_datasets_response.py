"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataLakeDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_dataset_list
    import aws_sdk_supplychain.types.data_lake_dataset_next_token


class ListDataLakeDatasetsResponse(TypedDict, closed=True):
    datasets: "aws_sdk_supplychain.types.data_lake_dataset_list.DataLakeDatasetList"
    """<p>The list of fetched dataset details.</p>"""
    next_token: NotRequired[
        "aws_sdk_supplychain.types.data_lake_dataset_next_token.DataLakeDatasetNextToken"
    ]
    """<p>The pagination token to fetch next page of datasets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakeDatasetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_lake_dataset_list

    out["datasets"] = aws_sdk_supplychain.types.data_lake_dataset_list.serialize_json(
        value["datasets"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataLakeDatasetsResponse:
    out: ListDataLakeDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "datasets" in data:
        import aws_sdk_supplychain.types.data_lake_dataset_list

        out["datasets"] = (
            aws_sdk_supplychain.types.data_lake_dataset_list.deserialize_json(
                data["datasets"]
            )
        )
    else:
        raise DeserializationError("ListDataLakeDatasetsResponse.datasets required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
