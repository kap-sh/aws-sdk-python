"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataSetReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.source
    import aws_sdk_iotsitewise.types.string


class DataSetReference(TypedDict):
    dataset_arn: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">ARN</a> of the dataset. The format is <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}</code>.</p>"""
    source: NotRequired["aws_sdk_iotsitewise.types.source.Source"]
    """<p>The data source for the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetReference) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "source" in value:
        import aws_sdk_iotsitewise.types.source

        out["source"] = aws_sdk_iotsitewise.types.source.serialize_json(value["source"])
    return out


def deserialize_json(data: dict) -> DataSetReference:
    out: DataSetReference = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    if "source" in data:
        import aws_sdk_iotsitewise.types.source

        out["source"] = aws_sdk_iotsitewise.types.source.deserialize_json(
            data["source"]
        )
    return out
