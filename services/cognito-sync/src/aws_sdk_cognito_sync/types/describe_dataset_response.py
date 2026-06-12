"""Generated from Smithy shape ``com.amazonaws.cognitosync#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.dataset


class DescribeDatasetResponse(TypedDict):
    dataset: NotRequired["aws_sdk_cognito_sync.types.dataset.Dataset"]
    """Meta data for a collection of data for an identity. An identity can have multiple datasets. A dataset can be general or associated with a particular entity in an application (like a saved game). Datasets are automatically created if they don't exist. Data is synced by dataset, and a dataset can hold up to 1MB of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset" in value:
        import aws_sdk_cognito_sync.types.dataset

        out["Dataset"] = aws_sdk_cognito_sync.types.dataset.serialize_json(
            value["dataset"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "Dataset" in data:
        import aws_sdk_cognito_sync.types.dataset

        out["dataset"] = aws_sdk_cognito_sync.types.dataset.deserialize_json(
            data["Dataset"]
        )
    return out
