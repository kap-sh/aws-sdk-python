"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.spot_fleet_request_config_data


class RequestSpotFleetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_config: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_config_data.SpotFleetRequestConfigData"
    ]
    """<p>The configuration for the Spot Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotFleetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "spot_fleet_request_config" in value:
        import aws_sdk_ec2.types.spot_fleet_request_config_data

        aws_sdk_ec2.types.spot_fleet_request_config_data.serialize_ec2_query(
            value["spot_fleet_request_config"],
            pairs,
            f"{prefix}.SpotFleetRequestConfig",
        )


def deserialize_ec2_query(el: Element) -> RequestSpotFleetRequest:
    out: RequestSpotFleetRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_spot_fleet_request_config = el.find("SpotFleetRequestConfig")
    if child_spot_fleet_request_config is not None:
        import aws_sdk_ec2.types.spot_fleet_request_config_data

        out["spot_fleet_request_config"] = (
            aws_sdk_ec2.types.spot_fleet_request_config_data.deserialize_ec2_query(
                child_spot_fleet_request_config
            )
        )
    return out
