"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_details
    import aws_sdk_dynamodb.types.source_table_details
    import aws_sdk_dynamodb.types.source_table_feature_details


class BackupDescription(TypedDict):
    backup_details: NotRequired["aws_sdk_dynamodb.types.backup_details.BackupDetails"]
    """<p>Contains the details of the backup created for the table. </p>"""
    source_table_details: NotRequired[
        "aws_sdk_dynamodb.types.source_table_details.SourceTableDetails"
    ]
    """<p>Contains the details of the table when the backup was created. </p>"""
    source_table_feature_details: NotRequired[
        "aws_sdk_dynamodb.types.source_table_feature_details.SourceTableFeatureDetails"
    ]
    """<p>Contains the details of the features enabled on the table when the backup was created. For example, LSIs, GSIs, streams, TTL.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupDescription) -> dict:
    out: dict = {}
    if "backup_details" in value:
        import aws_sdk_dynamodb.types.backup_details

        out["BackupDetails"] = (
            aws_sdk_dynamodb.types.backup_details.serialize_aws_json_1_0(
                value["backup_details"]
            )
        )
    if "source_table_details" in value:
        import aws_sdk_dynamodb.types.source_table_details

        out["SourceTableDetails"] = (
            aws_sdk_dynamodb.types.source_table_details.serialize_aws_json_1_0(
                value["source_table_details"]
            )
        )
    if "source_table_feature_details" in value:
        import aws_sdk_dynamodb.types.source_table_feature_details

        out["SourceTableFeatureDetails"] = (
            aws_sdk_dynamodb.types.source_table_feature_details.serialize_aws_json_1_0(
                value["source_table_feature_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BackupDescription:
    out: BackupDescription = {}  # type: ignore[typeddict-item]
    if "BackupDetails" in data:
        import aws_sdk_dynamodb.types.backup_details

        out["backup_details"] = (
            aws_sdk_dynamodb.types.backup_details.deserialize_aws_json_1_0(
                data["BackupDetails"]
            )
        )
    if "SourceTableDetails" in data:
        import aws_sdk_dynamodb.types.source_table_details

        out["source_table_details"] = (
            aws_sdk_dynamodb.types.source_table_details.deserialize_aws_json_1_0(
                data["SourceTableDetails"]
            )
        )
    if "SourceTableFeatureDetails" in data:
        import aws_sdk_dynamodb.types.source_table_feature_details

        out["source_table_feature_details"] = (
            aws_sdk_dynamodb.types.source_table_feature_details.deserialize_aws_json_1_0(
                data["SourceTableFeatureDetails"]
            )
        )
    return out
