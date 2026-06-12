"""Generated from Smithy shape ``com.amazonaws.firehose#SourceDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.database_source_description
    import aws_sdk_firehose.types.direct_put_source_description
    import aws_sdk_firehose.types.kinesis_stream_source_description
    import aws_sdk_firehose.types.msk_source_description


class SourceDescription(TypedDict):
    direct_put_source_description: NotRequired[
        "aws_sdk_firehose.types.direct_put_source_description.DirectPutSourceDescription"
    ]
    """<p>Details about Direct PUT used as the source for a Firehose stream. </p>"""
    kinesis_stream_source_description: NotRequired[
        "aws_sdk_firehose.types.kinesis_stream_source_description.KinesisStreamSourceDescription"
    ]
    """<p>The <a>KinesisStreamSourceDescription</a> value for the source Kinesis data stream.</p>"""
    msk_source_description: NotRequired[
        "aws_sdk_firehose.types.msk_source_description.MSKSourceDescription"
    ]
    """<p>The configuration description for the Amazon MSK cluster to be used as the source for a delivery stream.</p>"""
    database_source_description: NotRequired[
        "aws_sdk_firehose.types.database_source_description.DatabaseSourceDescription"
    ]
    """<p>Details about a database used as the source for a Firehose stream.</p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDescription) -> dict:
    out: dict = {}
    if "direct_put_source_description" in value:
        import aws_sdk_firehose.types.direct_put_source_description

        out["DirectPutSourceDescription"] = (
            aws_sdk_firehose.types.direct_put_source_description.serialize_aws_json_1_1(
                value["direct_put_source_description"]
            )
        )
    if "kinesis_stream_source_description" in value:
        import aws_sdk_firehose.types.kinesis_stream_source_description

        out["KinesisStreamSourceDescription"] = (
            aws_sdk_firehose.types.kinesis_stream_source_description.serialize_aws_json_1_1(
                value["kinesis_stream_source_description"]
            )
        )
    if "msk_source_description" in value:
        import aws_sdk_firehose.types.msk_source_description

        out["MSKSourceDescription"] = (
            aws_sdk_firehose.types.msk_source_description.serialize_aws_json_1_1(
                value["msk_source_description"]
            )
        )
    if "database_source_description" in value:
        import aws_sdk_firehose.types.database_source_description

        out["DatabaseSourceDescription"] = (
            aws_sdk_firehose.types.database_source_description.serialize_aws_json_1_1(
                value["database_source_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceDescription:
    out: SourceDescription = {}  # type: ignore[typeddict-item]
    if "DirectPutSourceDescription" in data:
        import aws_sdk_firehose.types.direct_put_source_description

        out["direct_put_source_description"] = (
            aws_sdk_firehose.types.direct_put_source_description.deserialize_aws_json_1_1(
                data["DirectPutSourceDescription"]
            )
        )
    if "KinesisStreamSourceDescription" in data:
        import aws_sdk_firehose.types.kinesis_stream_source_description

        out["kinesis_stream_source_description"] = (
            aws_sdk_firehose.types.kinesis_stream_source_description.deserialize_aws_json_1_1(
                data["KinesisStreamSourceDescription"]
            )
        )
    if "MSKSourceDescription" in data:
        import aws_sdk_firehose.types.msk_source_description

        out["msk_source_description"] = (
            aws_sdk_firehose.types.msk_source_description.deserialize_aws_json_1_1(
                data["MSKSourceDescription"]
            )
        )
    if "DatabaseSourceDescription" in data:
        import aws_sdk_firehose.types.database_source_description

        out["database_source_description"] = (
            aws_sdk_firehose.types.database_source_description.deserialize_aws_json_1_1(
                data["DatabaseSourceDescription"]
            )
        )
    return out
