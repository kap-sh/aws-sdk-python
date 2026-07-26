"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#IngestionInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.ingestion_s3_input_configuration


class IngestionInputConfiguration(TypedDict, closed=True):
    s3_input_configuration: "capo_lookoutequipment.types.ingestion_s3_input_configuration.IngestionS3InputConfiguration"
    """<p>The location information for the S3 bucket used for input data for the data ingestion. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionInputConfiguration) -> dict:
    out: dict = {}
    import capo_lookoutequipment.types.ingestion_s3_input_configuration

    out["S3InputConfiguration"] = (
        capo_lookoutequipment.types.ingestion_s3_input_configuration.serialize_aws_json_1_0(
            value["s3_input_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionInputConfiguration:
    out: IngestionInputConfiguration = {}  # type: ignore[typeddict-item]
    if "S3InputConfiguration" in data:
        import capo_lookoutequipment.types.ingestion_s3_input_configuration

        out["s3_input_configuration"] = (
            capo_lookoutequipment.types.ingestion_s3_input_configuration.deserialize_aws_json_1_0(
                data["S3InputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "IngestionInputConfiguration.s3_input_configuration required"
        )
    return out
