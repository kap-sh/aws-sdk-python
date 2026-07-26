"""Generated from Smithy shape ``com.amazonaws.networkmanager#GlobalNetwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.global_network_arn
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.global_network_state
    import capo_networkmanager.types.tag_list


class GlobalNetwork(TypedDict, closed=True):
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    global_network_arn: NotRequired[
        "capo_networkmanager.types.global_network_arn.GlobalNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the global network.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the global network.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the global network was created.</p>"""
    state: NotRequired[
        "capo_networkmanager.types.global_network_state.GlobalNetworkState"
    ]
    """<p>The state of the global network.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags for the global network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalNetwork) -> dict:
    out: dict = {}
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "global_network_arn" in value:
        out["GlobalNetworkArn"] = value["global_network_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.global_network_state

        out["State"] = capo_networkmanager.types.global_network_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GlobalNetwork:
    out: GlobalNetwork = {}  # type: ignore[typeddict-item]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "GlobalNetworkArn" in data:
        out["global_network_arn"] = data["GlobalNetworkArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "State" in data:
        import capo_networkmanager.types.global_network_state

        out["state"] = capo_networkmanager.types.global_network_state.deserialize_json(
            data["State"]
        )
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
