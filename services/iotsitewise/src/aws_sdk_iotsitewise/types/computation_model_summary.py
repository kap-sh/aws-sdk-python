"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.computation_model_status
    import aws_sdk_iotsitewise.types.computation_model_type
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.restricted_description
    import aws_sdk_iotsitewise.types.restricted_name
    import aws_sdk_iotsitewise.types.timestamp
    import aws_sdk_iotsitewise.types.version


class ComputationModelSummary(TypedDict, closed=True):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the computation model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}</code> </p>"""
    name: "aws_sdk_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the computation model.</p>"""
    description: NotRequired[
        "aws_sdk_iotsitewise.types.restricted_description.RestrictedDescription"
    ]
    """<p>The description of the computation model.</p>"""
    type: "aws_sdk_iotsitewise.types.computation_model_type.ComputationModelType"
    """<p>The type of the computation model.</p>"""
    creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The model creation date, in Unix epoch time.</p>"""
    last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the model was last updated, in Unix epoch time.</p>"""
    status: "aws_sdk_iotsitewise.types.computation_model_status.ComputationModelStatus"
    """<p>The current status of the computation model.</p>"""
    version: "aws_sdk_iotsitewise.types.version.Version"
    """<p>The version of the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_iotsitewise.types.computation_model_type

    out["type"] = aws_sdk_iotsitewise.types.computation_model_type.serialize_json(
        value["type"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["creationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["lastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    import aws_sdk_iotsitewise.types.computation_model_status

    out["status"] = aws_sdk_iotsitewise.types.computation_model_status.serialize_json(
        value["status"]
    )
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ComputationModelSummary:
    out: ComputationModelSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ComputationModelSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ComputationModelSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComputationModelSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_iotsitewise.types.computation_model_type

        out["type"] = aws_sdk_iotsitewise.types.computation_model_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ComputationModelSummary.type required")
    if "creationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["creation_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("ComputationModelSummary.creation_date required")
    if "lastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["last_update_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("ComputationModelSummary.last_update_date required")
    if "status" in data:
        import aws_sdk_iotsitewise.types.computation_model_status

        out["status"] = (
            aws_sdk_iotsitewise.types.computation_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ComputationModelSummary.status required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("ComputationModelSummary.version required")
    return out
