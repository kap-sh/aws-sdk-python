"""Generated from Smithy shape ``com.amazonaws.databrew#Metadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn


class Metadata(TypedDict, closed=True):
    source_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) associated with the dataset. Currently, DataBrew only supports ARNs from Amazon AppFlow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metadata) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    return out


def deserialize_json(data: dict) -> Metadata:
    out: Metadata = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    return out
