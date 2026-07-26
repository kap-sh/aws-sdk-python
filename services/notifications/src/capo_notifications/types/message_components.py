"""Generated from Smithy shape ``com.amazonaws.notifications#MessageComponents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.dimensions
    import capo_notifications.types.text_part_reference


class MessageComponents(TypedDict, closed=True):
    headline: NotRequired[
        "capo_notifications.types.text_part_reference.TextPartReference"
    ]
    """<p>A sentence long summary. For example, titles or an email subject line.</p>"""
    paragraph_summary: NotRequired[
        "capo_notifications.types.text_part_reference.TextPartReference"
    ]
    """<p>A paragraph long or multiple sentence summary. For example, Amazon Q Developer in chat applications notifications.</p>"""
    complete_description: NotRequired[
        "capo_notifications.types.text_part_reference.TextPartReference"
    ]
    """<p>A complete summary with all possible relevant information.</p>"""
    dimensions: NotRequired["capo_notifications.types.dimensions.Dimensions"]
    """<p>A list of properties in key-value pairs. Pairs are shown in order of importance from most important to least important. Channels may limit the number of dimensions shown to the notification viewer.</p> <note> <p>Included dimensions, keys, and values are subject to change.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageComponents) -> dict:
    out: dict = {}
    if "headline" in value:
        out["headline"] = value["headline"]
    if "paragraph_summary" in value:
        out["paragraphSummary"] = value["paragraph_summary"]
    if "complete_description" in value:
        out["completeDescription"] = value["complete_description"]
    if "dimensions" in value:
        import capo_notifications.types.dimensions

        out["dimensions"] = capo_notifications.types.dimensions.serialize_json(
            value["dimensions"]
        )
    return out


def deserialize_json(data: dict) -> MessageComponents:
    out: MessageComponents = {}  # type: ignore[typeddict-item]
    if "headline" in data:
        out["headline"] = data["headline"]
    if "paragraphSummary" in data:
        out["paragraph_summary"] = data["paragraphSummary"]
    if "completeDescription" in data:
        out["complete_description"] = data["completeDescription"]
    if "dimensions" in data:
        import capo_notifications.types.dimensions

        out["dimensions"] = capo_notifications.types.dimensions.deserialize_json(
            data["dimensions"]
        )
    return out
