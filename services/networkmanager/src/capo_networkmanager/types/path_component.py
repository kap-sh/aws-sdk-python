"""Generated from Smithy shape ``com.amazonaws.networkmanager#PathComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.integer
    import capo_networkmanager.types.network_resource_summary


class PathComponent(TypedDict, closed=True):
    sequence: NotRequired["capo_networkmanager.types.integer.Integer"]
    """<p>The sequence number in the path. The destination is 0.</p>"""
    resource: NotRequired[
        "capo_networkmanager.types.network_resource_summary.NetworkResourceSummary"
    ]
    """<p>The resource.</p>"""
    destination_cidr_block: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The destination CIDR block in the route table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathComponent) -> dict:
    out: dict = {}
    if "sequence" in value:
        out["Sequence"] = value["sequence"]
    if "resource" in value:
        import capo_networkmanager.types.network_resource_summary

        out["Resource"] = (
            capo_networkmanager.types.network_resource_summary.serialize_json(
                value["resource"]
            )
        )
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    return out


def deserialize_json(data: dict) -> PathComponent:
    out: PathComponent = {}  # type: ignore[typeddict-item]
    if "Sequence" in data:
        out["sequence"] = data["Sequence"]
    if "Resource" in data:
        import capo_networkmanager.types.network_resource_summary

        out["resource"] = (
            capo_networkmanager.types.network_resource_summary.deserialize_json(
                data["Resource"]
            )
        )
    if "DestinationCidrBlock" in data:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    return out
