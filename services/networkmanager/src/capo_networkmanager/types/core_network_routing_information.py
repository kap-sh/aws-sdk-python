"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkRoutingInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.constrained_string_list
    import capo_networkmanager.types.routing_information_next_hop


class CoreNetworkRoutingInformation(TypedDict, closed=True):
    prefix: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The IP prefix for the route.</p>"""
    next_hop: NotRequired[
        "capo_networkmanager.types.routing_information_next_hop.RoutingInformationNextHop"
    ]
    """<p>The next hop information for the route.</p>"""
    local_preference: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The BGP local preference value for the route.</p>"""
    med: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The BGP Multi-Exit Discriminator (MED) value for the route.</p>"""
    as_path: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The BGP AS path for the route.</p>"""
    communities: NotRequired[
        "capo_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The BGP community values for the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkRoutingInformation) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "next_hop" in value:
        import capo_networkmanager.types.routing_information_next_hop

        out["NextHop"] = (
            capo_networkmanager.types.routing_information_next_hop.serialize_json(
                value["next_hop"]
            )
        )
    if "local_preference" in value:
        out["LocalPreference"] = value["local_preference"]
    if "med" in value:
        out["Med"] = value["med"]
    if "as_path" in value:
        import capo_networkmanager.types.constrained_string_list

        out["AsPath"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["as_path"]
            )
        )
    if "communities" in value:
        import capo_networkmanager.types.constrained_string_list

        out["Communities"] = (
            capo_networkmanager.types.constrained_string_list.serialize_json(
                value["communities"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkRoutingInformation:
    out: CoreNetworkRoutingInformation = {}  # type: ignore[typeddict-item]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "NextHop" in data:
        import capo_networkmanager.types.routing_information_next_hop

        out["next_hop"] = (
            capo_networkmanager.types.routing_information_next_hop.deserialize_json(
                data["NextHop"]
            )
        )
    if "LocalPreference" in data:
        out["local_preference"] = data["LocalPreference"]
    if "Med" in data:
        out["med"] = data["Med"]
    if "AsPath" in data:
        import capo_networkmanager.types.constrained_string_list

        out["as_path"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["AsPath"]
            )
        )
    if "Communities" in data:
        import capo_networkmanager.types.constrained_string_list

        out["communities"] = (
            capo_networkmanager.types.constrained_string_list.deserialize_json(
                data["Communities"]
            )
        )
    return out
