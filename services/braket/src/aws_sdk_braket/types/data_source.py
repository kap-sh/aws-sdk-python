"""Generated from Smithy shape ``com.amazonaws.braket#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.s3_data_source


class DataSource(TypedDict, closed=True):
    s3_data_source: "aws_sdk_braket.types.s3_data_source.S3DataSource"
    """<p>Amazon S3 path of the input data used by the hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
    out: dict = {}
    import aws_sdk_braket.types.s3_data_source

    out["s3DataSource"] = aws_sdk_braket.types.s3_data_source.serialize_json(
        value["s3_data_source"]
    )
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "s3DataSource" in data:
        import aws_sdk_braket.types.s3_data_source

        out["s3_data_source"] = aws_sdk_braket.types.s3_data_source.deserialize_json(
            data["s3DataSource"]
        )
    else:
        raise DeserializationError("DataSource.s3_data_source required")
    return out
