"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Origination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean
    import aws_sdk_chime_sdk_voice.types.origination_route_list


class Origination(TypedDict, closed=True):
    routes: NotRequired[
        "aws_sdk_chime_sdk_voice.types.origination_route_list.OriginationRouteList"
    ]
    """<p>The call distribution properties defined for your SIP hosts. Valid range: Minimum value of 1. Maximum value of 20. This parameter is not required, but you must specify this parameter or <code>Disabled</code>.</p>"""
    disabled: NotRequired["aws_sdk_chime_sdk_voice.types.boolean.Boolean"]
    """<p>When origination settings are disabled, inbound calls are not enabled for your Amazon Chime SDK Voice Connector. This parameter is not required, but you must specify this parameter or <code>Routes</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Origination) -> dict:
    out: dict = {}
    if "routes" in value:
        import aws_sdk_chime_sdk_voice.types.origination_route_list

        out["Routes"] = (
            aws_sdk_chime_sdk_voice.types.origination_route_list.serialize_json(
                value["routes"]
            )
        )
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    return out


def deserialize_json(data: dict) -> Origination:
    out: Origination = {}  # type: ignore[typeddict-item]
    if "Routes" in data:
        import aws_sdk_chime_sdk_voice.types.origination_route_list

        out["routes"] = (
            aws_sdk_chime_sdk_voice.types.origination_route_list.deserialize_json(
                data["Routes"]
            )
        )
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    return out
