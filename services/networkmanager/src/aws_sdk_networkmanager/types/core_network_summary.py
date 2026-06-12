"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.aws_account_id
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_arn
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.core_network_state
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.tag_list


class CoreNetworkSummary(TypedDict):
    core_network_id: NotRequired[
        "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    core_network_arn: NotRequired[
        "aws_sdk_networkmanager.types.core_network_arn.CoreNetworkArn"
    ]
    """<p>a core network ARN.</p>"""
    global_network_id: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The global network ID.</p>"""
    owner_account_id: NotRequired[
        "aws_sdk_networkmanager.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the account owner.</p>"""
    state: NotRequired[
        "aws_sdk_networkmanager.types.core_network_state.CoreNetworkState"
    ]
    """<p>The state of a core network.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of a core network.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The key-value tags associated with a core network summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkSummary) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "core_network_arn" in value:
        out["CoreNetworkArn"] = value["core_network_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "state" in value:
        import aws_sdk_networkmanager.types.core_network_state

        out["State"] = aws_sdk_networkmanager.types.core_network_state.serialize_json(
            value["state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkSummary:
    out: CoreNetworkSummary = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "CoreNetworkArn" in data:
        out["core_network_arn"] = data["CoreNetworkArn"]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "State" in data:
        import aws_sdk_networkmanager.types.core_network_state

        out["state"] = aws_sdk_networkmanager.types.core_network_state.deserialize_json(
            data["State"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
