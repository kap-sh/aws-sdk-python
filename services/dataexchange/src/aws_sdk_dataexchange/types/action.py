"""Generated from Smithy shape ``com.amazonaws.dataexchange#Action``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.auto_export_revision_to_s3_request_details


class Action(TypedDict):
    export_revision_to_s3: NotRequired[
        "aws_sdk_dataexchange.types.auto_export_revision_to_s3_request_details.AutoExportRevisionToS3RequestDetails"
    ]
    """<p>Details for the export revision to Amazon S3 action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    if "export_revision_to_s3" in value:
        import aws_sdk_dataexchange.types.auto_export_revision_to_s3_request_details

        out["ExportRevisionToS3"] = (
            aws_sdk_dataexchange.types.auto_export_revision_to_s3_request_details.serialize_json(
                value["export_revision_to_s3"]
            )
        )
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if "ExportRevisionToS3" in data:
        import aws_sdk_dataexchange.types.auto_export_revision_to_s3_request_details

        out["export_revision_to_s3"] = (
            aws_sdk_dataexchange.types.auto_export_revision_to_s3_request_details.deserialize_json(
                data["ExportRevisionToS3"]
            )
        )
    return out
