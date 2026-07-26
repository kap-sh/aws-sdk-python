"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.dataset_status
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.restricted_description
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.timestamp


class DatasetSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    arn: "capo_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">ARN</a> of the dataset. The format is <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}</code>.</p>"""
    name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the dataset.</p>"""
    description: "capo_iotsitewise.types.restricted_description.RestrictedDescription"
    """<p>A description about the dataset, and its functionality.</p>"""
    creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The dataset creation date, in Unix epoch time.</p>"""
    last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dataset was last updated, in Unix epoch time.</p>"""
    status: "capo_iotsitewise.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. This contains the state and any error messages. The state is <code>ACTIVE</code> when ready to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_iotsitewise.types.timestamp

    out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    import capo_iotsitewise.types.dataset_status

    out["status"] = capo_iotsitewise.types.dataset_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DatasetSummary:
    out: DatasetSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DatasetSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DatasetSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DatasetSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("DatasetSummary.description required")
    if "creationDate" in data:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("DatasetSummary.creation_date required")
    if "lastUpdateDate" in data:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("DatasetSummary.last_update_date required")
    if "status" in data:
        import capo_iotsitewise.types.dataset_status

        out["status"] = capo_iotsitewise.types.dataset_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DatasetSummary.status required")
    return out
