"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.location
    import aws_sdk_iotsitewise.types.string


class Source(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>Contains the ARN of the dataset. If the source is Kendra, it's the ARN of the Kendra index.</p>"""
    location: NotRequired["aws_sdk_iotsitewise.types.location.Location"]
    """<p>Contains the location information where the cited text is originally stored. For example, if the data source is Kendra, and the text synchronized is from an S3 bucket, then the location refers to an S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "location" in value:
        import aws_sdk_iotsitewise.types.location

        out["location"] = aws_sdk_iotsitewise.types.location.serialize_json(
            value["location"]
        )
    return out


def deserialize_json(data: dict) -> Source:
    out: Source = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "location" in data:
        import aws_sdk_iotsitewise.types.location

        out["location"] = aws_sdk_iotsitewise.types.location.deserialize_json(
            data["location"]
        )
    return out
