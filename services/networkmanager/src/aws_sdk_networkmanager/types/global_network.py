"""Generated from Smithy shape ``com.amazonaws.networkmanager#GlobalNetwork``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.date_time
    import aws_sdk_networkmanager.types.global_network_arn
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.global_network_state
    import aws_sdk_networkmanager.types.tag_list


class GlobalNetwork(TypedDict):
    global_network_id: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    global_network_arn: NotRequired[
        "aws_sdk_networkmanager.types.global_network_arn.GlobalNetworkArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the global network.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the global network.</p>"""
    created_at: NotRequired["aws_sdk_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the global network was created.</p>"""
    state: NotRequired[
        "aws_sdk_networkmanager.types.global_network_state.GlobalNetworkState"
    ]
    """<p>The state of the global network.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
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
        import aws_sdk_networkmanager.types.date_time

        out["CreatedAt"] = aws_sdk_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import aws_sdk_networkmanager.types.global_network_state

        out["State"] = aws_sdk_networkmanager.types.global_network_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
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
        import aws_sdk_networkmanager.types.date_time

        out["created_at"] = aws_sdk_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "State" in data:
        import aws_sdk_networkmanager.types.global_network_state

        out["state"] = (
            aws_sdk_networkmanager.types.global_network_state.deserialize_json(
                data["State"]
            )
        )
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
