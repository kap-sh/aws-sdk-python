"""Generated from Smithy shape ``com.amazonaws.personalize#BatchSegmentJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.s3_data_config


class BatchSegmentJobOutput(TypedDict, closed=True):
    s3_data_destination: "capo_personalize.types.s3_data_config.S3DataConfig"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchSegmentJobOutput) -> dict:
    out: dict = {}
    import capo_personalize.types.s3_data_config

    out["s3DataDestination"] = (
        capo_personalize.types.s3_data_config.serialize_aws_json_1_1(
            value["s3_data_destination"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchSegmentJobOutput:
    out: BatchSegmentJobOutput = {}  # type: ignore[typeddict-item]
    if "s3DataDestination" in data:
        import capo_personalize.types.s3_data_config

        out["s3_data_destination"] = (
            capo_personalize.types.s3_data_config.deserialize_aws_json_1_1(
                data["s3DataDestination"]
            )
        )
    else:
        raise DeserializationError("BatchSegmentJobOutput.s3_data_destination required")
    return out
