"""Generated from Smithy shape ``com.amazonaws.braket#S3DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.s3_path


class S3DataSource(TypedDict, closed=True):
    s3_uri: "aws_sdk_braket.types.s3_path.S3Path"
    """<p>Depending on the value specified for the <code>S3DataType</code>, identifies either a key name prefix or a manifest that locates the S3 data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DataSource) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> S3DataSource:
    out: S3DataSource = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("S3DataSource.s3_uri required")
    return out
