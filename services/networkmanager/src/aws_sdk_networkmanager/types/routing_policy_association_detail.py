"""Generated from Smithy shape ``com.amazonaws.networkmanager#RoutingPolicyAssociationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string_list


class RoutingPolicyAssociationDetail(TypedDict):
    routing_policy_names: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The names of the routing policies in the association.</p>"""
    shared_segments: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The names of the segments that are shared with each other in the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingPolicyAssociationDetail) -> dict:
    out: dict = {}
    if "routing_policy_names" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["RoutingPolicyNames"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["routing_policy_names"]
            )
        )
    if "shared_segments" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["SharedSegments"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["shared_segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutingPolicyAssociationDetail:
    out: RoutingPolicyAssociationDetail = {}  # type: ignore[typeddict-item]
    if "RoutingPolicyNames" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["routing_policy_names"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["RoutingPolicyNames"]
            )
        )
    if "SharedSegments" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["shared_segments"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["SharedSegments"]
            )
        )
    return out
