"""Generated from Smithy shape ``com.amazonaws.databrew#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.dataset_list
    import aws_sdk_databrew.types.next_token


class ListDatasetsResponse(TypedDict, closed=True):
    datasets: "aws_sdk_databrew.types.dataset_list.DatasetList"
    """<p>A list of datasets that are defined.</p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.dataset_list

    out["Datasets"] = aws_sdk_databrew.types.dataset_list.serialize_json(
        value["datasets"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "Datasets" in data:
        import aws_sdk_databrew.types.dataset_list

        out["datasets"] = aws_sdk_databrew.types.dataset_list.deserialize_json(
            data["Datasets"]
        )
    else:
        raise DeserializationError("ListDatasetsResponse.datasets required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
