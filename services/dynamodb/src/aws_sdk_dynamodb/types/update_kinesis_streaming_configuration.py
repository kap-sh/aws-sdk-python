"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateKinesisStreamingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.approximate_creation_date_time_precision


class UpdateKinesisStreamingConfiguration(TypedDict):
    approximate_creation_date_time_precision: NotRequired[
        "aws_sdk_dynamodb.types.approximate_creation_date_time_precision.ApproximateCreationDateTimePrecision"
    ]
    """<p>Enables updating the precision of Kinesis data stream timestamp. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateKinesisStreamingConfiguration) -> dict:
    out: dict = {}
    if "approximate_creation_date_time_precision" in value:
        import aws_sdk_dynamodb.types.approximate_creation_date_time_precision

        out["ApproximateCreationDateTimePrecision"] = (
            aws_sdk_dynamodb.types.approximate_creation_date_time_precision.serialize_aws_json_1_0(
                value["approximate_creation_date_time_precision"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateKinesisStreamingConfiguration:
    out: UpdateKinesisStreamingConfiguration = {}  # type: ignore[typeddict-item]
    if "ApproximateCreationDateTimePrecision" in data:
        import aws_sdk_dynamodb.types.approximate_creation_date_time_precision

        out["approximate_creation_date_time_precision"] = (
            aws_sdk_dynamodb.types.approximate_creation_date_time_precision.deserialize_aws_json_1_0(
                data["ApproximateCreationDateTimePrecision"]
            )
        )
    return out
