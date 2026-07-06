"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ReferenceDataSourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.id
    import aws_sdk_kinesis_analytics_v2.types.in_app_table_name
    import aws_sdk_kinesis_analytics_v2.types.s3_reference_data_source_description
    import aws_sdk_kinesis_analytics_v2.types.source_schema


class ReferenceDataSourceDescription(TypedDict, closed=True):
    reference_id: "aws_sdk_kinesis_analytics_v2.types.id.Id"
    """<p>The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the <a>CreateApplication</a> or <a>UpdateApplication</a> operation.</p>"""
    table_name: "aws_sdk_kinesis_analytics_v2.types.in_app_table_name.InAppTableName"
    """<p>The in-application table name created by the specific reference data source configuration.</p>"""
    s3_reference_data_source_description: "aws_sdk_kinesis_analytics_v2.types.s3_reference_data_source_description.S3ReferenceDataSourceDescription"
    """<p>Provides the Amazon S3 bucket name, the object key name that contains the reference data. </p>"""
    reference_schema: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.source_schema.SourceSchema"
    ]
    """<p>Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSourceDescription) -> dict:
    out: dict = {}
    out["ReferenceId"] = value["reference_id"]
    out["TableName"] = value["table_name"]
    import aws_sdk_kinesis_analytics_v2.types.s3_reference_data_source_description

    out["S3ReferenceDataSourceDescription"] = (
        aws_sdk_kinesis_analytics_v2.types.s3_reference_data_source_description.serialize_aws_json_1_1(
            value["s3_reference_data_source_description"]
        )
    )
    if "reference_schema" in value:
        import aws_sdk_kinesis_analytics_v2.types.source_schema

        out["ReferenceSchema"] = (
            aws_sdk_kinesis_analytics_v2.types.source_schema.serialize_aws_json_1_1(
                value["reference_schema"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferenceDataSourceDescription:
    out: ReferenceDataSourceDescription = {}  # type: ignore[typeddict-item]
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    else:
        raise DeserializationError(
            "ReferenceDataSourceDescription.reference_id required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("ReferenceDataSourceDescription.table_name required")
    if "S3ReferenceDataSourceDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_reference_data_source_description

        out["s3_reference_data_source_description"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_reference_data_source_description.deserialize_aws_json_1_1(
                data["S3ReferenceDataSourceDescription"]
            )
        )
    else:
        raise DeserializationError(
            "ReferenceDataSourceDescription.s3_reference_data_source_description required"
        )
    if "ReferenceSchema" in data:
        import aws_sdk_kinesis_analytics_v2.types.source_schema

        out["reference_schema"] = (
            aws_sdk_kinesis_analytics_v2.types.source_schema.deserialize_aws_json_1_1(
                data["ReferenceSchema"]
            )
        )
    return out
