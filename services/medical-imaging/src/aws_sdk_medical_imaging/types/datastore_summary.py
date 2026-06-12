"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.arn
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.datastore_name
    import aws_sdk_medical_imaging.types.datastore_status
    import aws_sdk_medical_imaging.types.date


class DatastoreSummary(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_name: "aws_sdk_medical_imaging.types.datastore_name.DatastoreName"
    """<p>The data store name.</p>"""
    datastore_status: "aws_sdk_medical_imaging.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""
    datastore_arn: NotRequired["aws_sdk_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the data store.</p>"""
    created_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was created.</p>"""
    updated_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatastoreSummary) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["datastoreName"] = value["datastore_name"]
    import aws_sdk_medical_imaging.types.datastore_status

    out["datastoreStatus"] = (
        aws_sdk_medical_imaging.types.datastore_status.serialize_json(
            value["datastore_status"]
        )
    )
    if "datastore_arn" in value:
        out["datastoreArn"] = value["datastore_arn"]
    if "created_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["createdAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["updatedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DatastoreSummary:
    out: DatastoreSummary = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("DatastoreSummary.datastore_id required")
    if "datastoreName" in data:
        out["datastore_name"] = data["datastoreName"]
    else:
        raise DeserializationError("DatastoreSummary.datastore_name required")
    if "datastoreStatus" in data:
        import aws_sdk_medical_imaging.types.datastore_status

        out["datastore_status"] = (
            aws_sdk_medical_imaging.types.datastore_status.deserialize_json(
                data["datastoreStatus"]
            )
        )
    else:
        raise DeserializationError("DatastoreSummary.datastore_status required")
    if "datastoreArn" in data:
        out["datastore_arn"] = data["datastoreArn"]
    if "createdAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["created_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["updated_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["updatedAt"]
        )
    return out
