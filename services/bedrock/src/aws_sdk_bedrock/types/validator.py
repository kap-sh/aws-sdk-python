"""Generated from Smithy shape ``com.amazonaws.bedrock#Validator``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.s3_uri


class Validator(TypedDict, closed=True):
    s3_uri: "aws_sdk_bedrock.types.s3_uri.S3Uri"
    """<p>The S3 URI where the validation data is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Validator) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> Validator:
    out: Validator = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("Validator.s3_uri required")
    return out
