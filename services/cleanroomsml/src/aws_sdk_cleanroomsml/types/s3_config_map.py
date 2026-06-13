"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#S3ConfigMap``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.s3_path


class S3ConfigMap(TypedDict):
    s3_uri: "aws_sdk_cleanroomsml.types.s3_path.S3Path"
    """<p>The Amazon S3 location URI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ConfigMap) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> S3ConfigMap:
    out: S3ConfigMap = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("S3ConfigMap.s3_uri required")
    return out
