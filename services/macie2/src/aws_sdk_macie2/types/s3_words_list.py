"""Generated from Smithy shape ``com.amazonaws.macie2#S3WordsList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string_min1_max1024_pattern_ss
    import aws_sdk_macie2.types.__string_min3_max255_pattern_a_za_z093255


class S3WordsList(TypedDict):
    bucket_name: NotRequired[
        "aws_sdk_macie2.types.__string_min3_max255_pattern_a_za_z093255.__stringMin3Max255PatternAZaZ093255"
    ]
    """<p>The full name of the S3 bucket that contains the object.</p>"""
    object_key: NotRequired[
        "aws_sdk_macie2.types.__string_min1_max1024_pattern_ss.__stringMin1Max1024PatternSS"
    ]
    """<p>The full name (key) of the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3WordsList) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "object_key" in value:
        out["objectKey"] = value["object_key"]
    return out


def deserialize_json(data: dict) -> S3WordsList:
    out: S3WordsList = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "objectKey" in data:
        out["object_key"] = data["objectKey"]
    return out
