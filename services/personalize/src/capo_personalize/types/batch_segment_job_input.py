"""Generated from Smithy shape ``com.amazonaws.personalize#BatchSegmentJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.s3_data_config


class BatchSegmentJobInput(TypedDict, closed=True):
    s3_data_source: "capo_personalize.types.s3_data_config.S3DataConfig"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchSegmentJobInput) -> dict:
    out: dict = {}
    import capo_personalize.types.s3_data_config

    out["s3DataSource"] = capo_personalize.types.s3_data_config.serialize_aws_json_1_1(
        value["s3_data_source"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchSegmentJobInput:
    out: BatchSegmentJobInput = {}  # type: ignore[typeddict-item]
    if "s3DataSource" in data:
        import capo_personalize.types.s3_data_config

        out["s3_data_source"] = (
            capo_personalize.types.s3_data_config.deserialize_aws_json_1_1(
                data["s3DataSource"]
            )
        )
    else:
        raise DeserializationError("BatchSegmentJobInput.s3_data_source required")
    return out
