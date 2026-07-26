"""Generated from Smithy shape ``com.amazonaws.forecast#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.s3_config


class DataSource(TypedDict, closed=True):
    s3_config: "capo_forecast.types.s3_config.S3Config"
    """<p>The path to the data stored in an Amazon Simple Storage Service (Amazon S3) bucket along with the credentials to access the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> dict:
    out: dict = {}
    import capo_forecast.types.s3_config

    out["S3Config"] = capo_forecast.types.s3_config.serialize_aws_json_1_1(
        value["s3_config"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "S3Config" in data:
        import capo_forecast.types.s3_config

        out["s3_config"] = capo_forecast.types.s3_config.deserialize_aws_json_1_1(
            data["S3Config"]
        )
    else:
        raise DeserializationError("DataSource.s3_config required")
    return out
