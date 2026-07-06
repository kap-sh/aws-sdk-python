"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.dataset_source
    import aws_sdk_iotsitewise.types.dataset_status
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.restricted_description
    import aws_sdk_iotsitewise.types.restricted_name
    import aws_sdk_iotsitewise.types.timestamp
    import aws_sdk_iotsitewise.types.version


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    dataset_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">ARN</a> of the dataset. The format is <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}</code>.</p>"""
    dataset_name: "aws_sdk_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the dataset.</p>"""
    dataset_description: (
        "aws_sdk_iotsitewise.types.restricted_description.RestrictedDescription"
    )
    """<p>A description about the dataset, and its functionality.</p>"""
    dataset_source: "aws_sdk_iotsitewise.types.dataset_source.DatasetSource"
    """<p>The data source for the dataset.</p>"""
    dataset_status: "aws_sdk_iotsitewise.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. This contains the state and any error messages. State is <code>CREATING</code> after a successfull call to this API, and any associated error message. The state is <code>ACTIVE</code> when ready to use.</p>"""
    dataset_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The dataset creation date, in Unix epoch time.</p>"""
    dataset_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dataset was last updated, in Unix epoch time.</p>"""
    dataset_version: NotRequired["aws_sdk_iotsitewise.types.version.Version"]
    """<p>The version of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    out["datasetArn"] = value["dataset_arn"]
    out["datasetName"] = value["dataset_name"]
    out["datasetDescription"] = value["dataset_description"]
    import aws_sdk_iotsitewise.types.dataset_source

    out["datasetSource"] = aws_sdk_iotsitewise.types.dataset_source.serialize_json(
        value["dataset_source"]
    )
    import aws_sdk_iotsitewise.types.dataset_status

    out["datasetStatus"] = aws_sdk_iotsitewise.types.dataset_status.serialize_json(
        value["dataset_status"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["datasetCreationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["dataset_creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["datasetLastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["dataset_last_update_date"]
    )
    if "dataset_version" in value:
        out["datasetVersion"] = value["dataset_version"]
    return out


def deserialize_json(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_id required")
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_arn required")
    if "datasetName" in data:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_name required")
    if "datasetDescription" in data:
        out["dataset_description"] = data["datasetDescription"]
    else:
        raise DeserializationError(
            "DescribeDatasetResponse.dataset_description required"
        )
    if "datasetSource" in data:
        import aws_sdk_iotsitewise.types.dataset_source

        out["dataset_source"] = (
            aws_sdk_iotsitewise.types.dataset_source.deserialize_json(
                data["datasetSource"]
            )
        )
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_source required")
    if "datasetStatus" in data:
        import aws_sdk_iotsitewise.types.dataset_status

        out["dataset_status"] = (
            aws_sdk_iotsitewise.types.dataset_status.deserialize_json(
                data["datasetStatus"]
            )
        )
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_status required")
    if "datasetCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["dataset_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["datasetCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDatasetResponse.dataset_creation_date required"
        )
    if "datasetLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["dataset_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["datasetLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDatasetResponse.dataset_last_update_date required"
        )
    if "datasetVersion" in data:
        out["dataset_version"] = data["datasetVersion"]
    return out
