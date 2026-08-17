"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_details
    import capo_dynamodb.types.source_table_details
    import capo_dynamodb.types.source_table_feature_details


class BackupDescription(TypedDict, closed=True):
    backup_details: NotRequired["capo_dynamodb.types.backup_details.BackupDetails"]
    """<p>Contains the details of the backup created for the table. </p>"""
    source_table_details: NotRequired[
        "capo_dynamodb.types.source_table_details.SourceTableDetails"
    ]
    """<p>Contains the details of the table when the backup was created. </p>"""
    source_table_feature_details: NotRequired[
        "capo_dynamodb.types.source_table_feature_details.SourceTableFeatureDetails"
    ]
    """<p>Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupDescription) -> dict:
    out: dict = {}
    if "backup_details" in value:
        import capo_dynamodb.types.backup_details

        out["BackupDetails"] = (
            capo_dynamodb.types.backup_details.serialize_aws_json_1_0(
                value["backup_details"]
            )
        )
    if "source_table_details" in value:
        import capo_dynamodb.types.source_table_details

        out["SourceTableDetails"] = (
            capo_dynamodb.types.source_table_details.serialize_aws_json_1_0(
                value["source_table_details"]
            )
        )
    if "source_table_feature_details" in value:
        import capo_dynamodb.types.source_table_feature_details

        out["SourceTableFeatureDetails"] = (
            capo_dynamodb.types.source_table_feature_details.serialize_aws_json_1_0(
                value["source_table_feature_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BackupDescription:
    out: BackupDescription = {}  # type: ignore[typeddict-item]
    if data.get("BackupDetails") is not None:
        import capo_dynamodb.types.backup_details

        out["backup_details"] = (
            capo_dynamodb.types.backup_details.deserialize_aws_json_1_0(
                data["BackupDetails"]
            )
        )
    if data.get("SourceTableDetails") is not None:
        import capo_dynamodb.types.source_table_details

        out["source_table_details"] = (
            capo_dynamodb.types.source_table_details.deserialize_aws_json_1_0(
                data["SourceTableDetails"]
            )
        )
    if data.get("SourceTableFeatureDetails") is not None:
        import capo_dynamodb.types.source_table_feature_details

        out["source_table_feature_details"] = (
            capo_dynamodb.types.source_table_feature_details.deserialize_aws_json_1_0(
                data["SourceTableFeatureDetails"]
            )
        )
    return out
