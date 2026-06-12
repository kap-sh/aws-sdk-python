"""Generated from Smithy shape ``com.amazonaws.networkmanager#ServiceInsertionSegments``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string_list


class ServiceInsertionSegments(TypedDict):
    send_via: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The list of segments associated with the <code>send-via</code> action.</p>"""
    send_to: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The list of segments associated with the <code>send-to</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceInsertionSegments) -> dict:
    out: dict = {}
    if "send_via" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["SendVia"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["send_via"]
            )
        )
    if "send_to" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["SendTo"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["send_to"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceInsertionSegments:
    out: ServiceInsertionSegments = {}  # type: ignore[typeddict-item]
    if "SendVia" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["send_via"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["SendVia"]
            )
        )
    if "SendTo" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["send_to"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["SendTo"]
            )
        )
    return out
