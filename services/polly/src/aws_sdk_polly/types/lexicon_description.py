"""Generated from Smithy shape ``com.amazonaws.polly#LexiconDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.lexicon_attributes
    import aws_sdk_polly.types.lexicon_name


class LexiconDescription(TypedDict, closed=True):
    name: NotRequired["aws_sdk_polly.types.lexicon_name.LexiconName"]
    """<p>Name of the lexicon.</p>"""
    attributes: NotRequired["aws_sdk_polly.types.lexicon_attributes.LexiconAttributes"]
    """<p>Provides lexicon metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexiconDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "attributes" in value:
        import aws_sdk_polly.types.lexicon_attributes

        out["Attributes"] = aws_sdk_polly.types.lexicon_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> LexiconDescription:
    out: LexiconDescription = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Attributes" in data:
        import aws_sdk_polly.types.lexicon_attributes

        out["attributes"] = aws_sdk_polly.types.lexicon_attributes.deserialize_json(
            data["Attributes"]
        )
    return out
