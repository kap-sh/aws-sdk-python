"""Generated from Smithy shape ``com.amazonaws.networkmanager#ServiceInsertionSegments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string_list


class ServiceInsertionSegments(TypedDict, closed=True):
    send_via: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The list of segments associated with the <code>send-via</code> action.</p>"""
    send_to: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The list of segments associated with the <code>send-to</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceInsertionSegments) -> dict:
    out: dict = {}
    if "send_via" in value:
        import capo_networkmanager.types.constrained_string_list

        out["SendVia"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["send_via"]
            )
        )
    if "send_to" in value:
        import capo_networkmanager.types.constrained_string_list

        out["SendTo"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["send_to"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceInsertionSegments:
    out: ServiceInsertionSegments = {}  # type: ignore[typeddict-item]
    if "SendVia" in data:
        import capo_networkmanager.types.constrained_string_list

        out["send_via"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["SendVia"]
            )
        )
    if "SendTo" in data:
        import capo_networkmanager.types.constrained_string_list

        out["send_to"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["SendTo"]
            )
        )
    return out
