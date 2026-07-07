"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportRevisionsToS3ResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.export_server_side_encryption
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.list_of_revision_destination_entry


class ExportRevisionsToS3ResponseDetails(TypedDict, closed=True):
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    encryption: NotRequired[
        "aws_sdk_dataexchange.types.export_server_side_encryption.ExportServerSideEncryption"
    ]
    """<p>Encryption configuration of the export job.</p>"""
    revision_destinations: "aws_sdk_dataexchange.types.list_of_revision_destination_entry.ListOfRevisionDestinationEntry"
    """<p>The destination in Amazon S3 where the revision is exported.</p>"""
    event_action_arn: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the event action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportRevisionsToS3ResponseDetails) -> dict:
    out: dict = {}
    out["DataSetId"] = value["data_set_id"]
    if "encryption" in value:
        import aws_sdk_dataexchange.types.export_server_side_encryption

        out["Encryption"] = (
            aws_sdk_dataexchange.types.export_server_side_encryption.serialize_json(
                value["encryption"]
            )
        )
    import aws_sdk_dataexchange.types.list_of_revision_destination_entry

    out["RevisionDestinations"] = (
        aws_sdk_dataexchange.types.list_of_revision_destination_entry.serialize_json(
            value["revision_destinations"]
        )
    )
    if "event_action_arn" in value:
        out["EventActionArn"] = value["event_action_arn"]
    return out


def deserialize_json(data: dict) -> ExportRevisionsToS3ResponseDetails:
    out: ExportRevisionsToS3ResponseDetails = {}  # type: ignore[typeddict-item]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ExportRevisionsToS3ResponseDetails.data_set_id required"
        )
    if "Encryption" in data:
        import aws_sdk_dataexchange.types.export_server_side_encryption

        out["encryption"] = (
            aws_sdk_dataexchange.types.export_server_side_encryption.deserialize_json(
                data["Encryption"]
            )
        )
    if "RevisionDestinations" in data:
        import aws_sdk_dataexchange.types.list_of_revision_destination_entry

        out["revision_destinations"] = (
            aws_sdk_dataexchange.types.list_of_revision_destination_entry.deserialize_json(
                data["RevisionDestinations"]
            )
        )
    else:
        raise DeserializationError(
            "ExportRevisionsToS3ResponseDetails.revision_destinations required"
        )
    if "EventActionArn" in data:
        out["event_action_arn"] = data["EventActionArn"]
    return out
