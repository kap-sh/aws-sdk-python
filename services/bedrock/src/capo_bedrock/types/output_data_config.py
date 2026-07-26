"""Generated from Smithy shape ``com.amazonaws.bedrock#OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.s3_uri


class OutputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_bedrock.types.s3_uri.S3Uri"
    """<p>The S3 URI where the output data is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputDataConfig) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> OutputDataConfig:
    out: OutputDataConfig = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("OutputDataConfig.s3_uri required")
    return out
