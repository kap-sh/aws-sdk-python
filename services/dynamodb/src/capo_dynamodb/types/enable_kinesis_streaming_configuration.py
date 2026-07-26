"""Generated from Smithy shape ``com.amazonaws.dynamodb#EnableKinesisStreamingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.approximate_creation_date_time_precision


class EnableKinesisStreamingConfiguration(TypedDict, closed=True):
    approximate_creation_date_time_precision: NotRequired[
        "capo_dynamodb.types.approximate_creation_date_time_precision.ApproximateCreationDateTimePrecision"
    ]
    """<p>Toggle for the precision of Kinesis data stream timestamp. The values are either <code>MILLISECOND</code> or <code>MICROSECOND</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnableKinesisStreamingConfiguration) -> dict:
    out: dict = {}
    if "approximate_creation_date_time_precision" in value:
        import capo_dynamodb.types.approximate_creation_date_time_precision

        out["ApproximateCreationDateTimePrecision"] = (
            capo_dynamodb.types.approximate_creation_date_time_precision.serialize_aws_json_1_0(
                value["approximate_creation_date_time_precision"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnableKinesisStreamingConfiguration:
    out: EnableKinesisStreamingConfiguration = {}  # type: ignore[typeddict-item]
    if "ApproximateCreationDateTimePrecision" in data:
        import capo_dynamodb.types.approximate_creation_date_time_precision

        out["approximate_creation_date_time_precision"] = (
            capo_dynamodb.types.approximate_creation_date_time_precision.deserialize_aws_json_1_0(
                data["ApproximateCreationDateTimePrecision"]
            )
        )
    return out
