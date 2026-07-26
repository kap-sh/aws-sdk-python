"""Generated from Smithy shape ``com.amazonaws.dataexchange#AutoExportRevisionToS3RequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.auto_export_revision_destination_entry
    import capo_dataexchange.types.export_server_side_encryption


class AutoExportRevisionToS3RequestDetails(TypedDict, closed=True):
    encryption: NotRequired[
        "capo_dataexchange.types.export_server_side_encryption.ExportServerSideEncryption"
    ]
    """<p>Encryption configuration for the auto export job.</p>"""
    revision_destination: "capo_dataexchange.types.auto_export_revision_destination_entry.AutoExportRevisionDestinationEntry"
    """<p>A revision destination is the Amazon S3 bucket folder destination to where the export will be sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoExportRevisionToS3RequestDetails) -> dict:
    out: dict = {}
    if "encryption" in value:
        import capo_dataexchange.types.export_server_side_encryption

        out["Encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.serialize_json(
                value["encryption"]
            )
        )
    import capo_dataexchange.types.auto_export_revision_destination_entry

    out["RevisionDestination"] = (
        capo_dataexchange.types.auto_export_revision_destination_entry.serialize_json(
            value["revision_destination"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutoExportRevisionToS3RequestDetails:
    out: AutoExportRevisionToS3RequestDetails = {}  # type: ignore[typeddict-item]
    if "Encryption" in data:
        import capo_dataexchange.types.export_server_side_encryption

        out["encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.deserialize_json(
                data["Encryption"]
            )
        )
    if "RevisionDestination" in data:
        import capo_dataexchange.types.auto_export_revision_destination_entry

        out["revision_destination"] = (
            capo_dataexchange.types.auto_export_revision_destination_entry.deserialize_json(
                data["RevisionDestination"]
            )
        )
    else:
        raise DeserializationError(
            "AutoExportRevisionToS3RequestDetails.revision_destination required"
        )
    return out
