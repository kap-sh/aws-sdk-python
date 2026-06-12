"""Generated from Smithy shape ``com.amazonaws.databrew#Sample``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.sample_size
    import aws_sdk_databrew.types.sample_type


class Sample(TypedDict):
    size: NotRequired["aws_sdk_databrew.types.sample_size.SampleSize"]
    """<p>The number of rows in the sample.</p>"""
    type: "aws_sdk_databrew.types.sample_type.SampleType"
    """<p>The way in which DataBrew obtains rows from a dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sample) -> dict:
    out: dict = {}
    if "size" in value:
        out["Size"] = value["size"]
    import aws_sdk_databrew.types.sample_type

    out["Type"] = aws_sdk_databrew.types.sample_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Sample:
    out: Sample = {}  # type: ignore[typeddict-item]
    if "Size" in data:
        out["size"] = data["Size"]
    if "Type" in data:
        import aws_sdk_databrew.types.sample_type

        out["type"] = aws_sdk_databrew.types.sample_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("Sample.type required")
    return out
