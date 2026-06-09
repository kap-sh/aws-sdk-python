"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelLogOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cloud_watch_log_options


class VpnTunnelLogOptions(TypedDict):
    cloud_watch_log_options: NotRequired[
        "aws_sdk_ec2.types.cloud_watch_log_options.CloudWatchLogOptions"
    ]
    """<p>Options for sending VPN tunnel logs to CloudWatch.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnTunnelLogOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cloud_watch_log_options" in value:
        import aws_sdk_ec2.types.cloud_watch_log_options

        aws_sdk_ec2.types.cloud_watch_log_options.serialize_ec2_query(
            value["cloud_watch_log_options"], pairs, f"{prefix}.CloudWatchLogOptions"
        )


def deserialize_ec2_query(el: Element) -> VpnTunnelLogOptions:
    out: VpnTunnelLogOptions = {}  # type: ignore[typeddict-item]
    child_cloud_watch_log_options = el.find("CloudWatchLogOptions")
    if child_cloud_watch_log_options is not None:
        import aws_sdk_ec2.types.cloud_watch_log_options

        out["cloud_watch_log_options"] = (
            aws_sdk_ec2.types.cloud_watch_log_options.deserialize_ec2_query(
                child_cloud_watch_log_options
            )
        )
    return out
