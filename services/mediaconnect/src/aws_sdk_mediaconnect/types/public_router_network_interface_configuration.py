"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicRouterNetworkInterfaceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.network_interface_rule_list


class PublicRouterNetworkInterfaceConfiguration(TypedDict, closed=True):
    allow_rules: "aws_sdk_mediaconnect.types.network_interface_rule_list.NetworkInterfaceRuleList"
    """<p>The list of allowed CIDR blocks for the public router network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicRouterNetworkInterfaceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.network_interface_rule_list

    out["allowRules"] = (
        aws_sdk_mediaconnect.types.network_interface_rule_list.serialize_json(
            value["allow_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> PublicRouterNetworkInterfaceConfiguration:
    out: PublicRouterNetworkInterfaceConfiguration = {}  # type: ignore[typeddict-item]
    if "allowRules" in data:
        import aws_sdk_mediaconnect.types.network_interface_rule_list

        out["allow_rules"] = (
            aws_sdk_mediaconnect.types.network_interface_rule_list.deserialize_json(
                data["allowRules"]
            )
        )
    else:
        raise DeserializationError(
            "PublicRouterNetworkInterfaceConfiguration.allow_rules required"
        )
    return out
