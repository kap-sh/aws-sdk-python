"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMarketOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.market_type_enum
    import aws_sdk_workspaces_instances.types.spot_market_options


class InstanceMarketOptionsRequest(TypedDict):
    market_type: NotRequired[
        "aws_sdk_workspaces_instances.types.market_type_enum.MarketTypeEnum"
    ]
    """<p>Specifies the type of marketplace for instance deployment.</p>"""
    spot_options: NotRequired[
        "aws_sdk_workspaces_instances.types.spot_market_options.SpotMarketOptions"
    ]
    """<p>Configuration options for spot instance deployment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceMarketOptionsRequest) -> dict:
    out: dict = {}
    if "market_type" in value:
        import aws_sdk_workspaces_instances.types.market_type_enum

        out["MarketType"] = (
            aws_sdk_workspaces_instances.types.market_type_enum.serialize_aws_json_1_0(
                value["market_type"]
            )
        )
    if "spot_options" in value:
        import aws_sdk_workspaces_instances.types.spot_market_options

        out["SpotOptions"] = (
            aws_sdk_workspaces_instances.types.spot_market_options.serialize_aws_json_1_0(
                value["spot_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceMarketOptionsRequest:
    out: InstanceMarketOptionsRequest = {}  # type: ignore[typeddict-item]
    if "MarketType" in data:
        import aws_sdk_workspaces_instances.types.market_type_enum

        out["market_type"] = (
            aws_sdk_workspaces_instances.types.market_type_enum.deserialize_aws_json_1_0(
                data["MarketType"]
            )
        )
    if "SpotOptions" in data:
        import aws_sdk_workspaces_instances.types.spot_market_options

        out["spot_options"] = (
            aws_sdk_workspaces_instances.types.spot_market_options.deserialize_aws_json_1_0(
                data["SpotOptions"]
            )
        )
    return out
