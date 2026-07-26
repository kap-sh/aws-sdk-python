"""Generated from Smithy shape ``com.amazonaws.networkmanager#WhenSentTo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.when_sent_to_segments_list


class WhenSentTo(TypedDict, closed=True):
    when_sent_to_segments_list: NotRequired[
        "capo_networkmanager.types.when_sent_to_segments_list.WhenSentToSegmentsList"
    ]
    """<p>The list of destination segments when the service insertion action is <code>send-to</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhenSentTo) -> dict:
    out: dict = {}
    if "when_sent_to_segments_list" in value:
        import capo_networkmanager.types.when_sent_to_segments_list

        out["WhenSentToSegmentsList"] = (
            capo_networkmanager.types.when_sent_to_segments_list.serialize_json(
                value["when_sent_to_segments_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> WhenSentTo:
    out: WhenSentTo = {}  # type: ignore[typeddict-item]
    if "WhenSentToSegmentsList" in data:
        import capo_networkmanager.types.when_sent_to_segments_list

        out["when_sent_to_segments_list"] = (
            capo_networkmanager.types.when_sent_to_segments_list.deserialize_json(
                data["WhenSentToSegmentsList"]
            )
        )
    return out
