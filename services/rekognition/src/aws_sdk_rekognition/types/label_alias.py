"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelAlias``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string


class LabelAlias(TypedDict):
    name: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The name of an alias for a given label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelAlias) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelAlias:
    out: LabelAlias = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
