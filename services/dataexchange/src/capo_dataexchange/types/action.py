"""Generated from Smithy shape ``com.amazonaws.dataexchange#Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.auto_export_revision_to_s3_request_details


class Action(TypedDict, closed=True):
    export_revision_to_s3: NotRequired[
        "capo_dataexchange.types.auto_export_revision_to_s3_request_details.AutoExportRevisionToS3RequestDetails"
    ]
    """<p>Details for the export revision to Amazon S3 action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    if "export_revision_to_s3" in value:
        import capo_dataexchange.types.auto_export_revision_to_s3_request_details

        out["ExportRevisionToS3"] = (
            capo_dataexchange.types.auto_export_revision_to_s3_request_details.serialize_json(
                value["export_revision_to_s3"]
            )
        )
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if "ExportRevisionToS3" in data:
        import capo_dataexchange.types.auto_export_revision_to_s3_request_details

        out["export_revision_to_s3"] = (
            capo_dataexchange.types.auto_export_revision_to_s3_request_details.deserialize_json(
                data["ExportRevisionToS3"]
            )
        )
    return out
