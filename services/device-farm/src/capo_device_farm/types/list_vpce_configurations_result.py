"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListVPCEConfigurationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.pagination_token
    import capo_device_farm.types.vpce_configurations


class ListVPCEConfigurationsResult(TypedDict, closed=True):
    vpce_configurations: NotRequired[
        "capo_device_farm.types.vpce_configurations.VPCEConfigurations"
    ]
    """<p>An array of <code>VPCEConfiguration</code> objects that contain information about your VPC endpoint configuration.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVPCEConfigurationsResult) -> dict:
    out: dict = {}
    if "vpce_configurations" in value:
        import capo_device_farm.types.vpce_configurations

        out["vpceConfigurations"] = (
            capo_device_farm.types.vpce_configurations.serialize_aws_json_1_1(
                value["vpce_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVPCEConfigurationsResult:
    out: ListVPCEConfigurationsResult = {}  # type: ignore[typeddict-item]
    if "vpceConfigurations" in data:
        import capo_device_farm.types.vpce_configurations

        out["vpce_configurations"] = (
            capo_device_farm.types.vpce_configurations.deserialize_aws_json_1_1(
                data["vpceConfigurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
