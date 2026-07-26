"""Generated from Smithy shape ``com.amazonaws.ec2#CloudWatchLogOptionsSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.cloud_watch_log_group_arn
    import capo_ec2.types.string


class CloudWatchLogOptionsSpecification(TypedDict, closed=True):
    log_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enable or disable VPN tunnel logging feature. Default value is <code>False</code>.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    log_group_arn: NotRequired[
        "capo_ec2.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch log group to send logs to.</p>"""
    log_output_format: NotRequired["capo_ec2.types.string.String"]
    """<p>Set log format. Default format is <code>json</code>.</p> <p>Valid values: <code>json</code> | <code>text</code> </p>"""
    bgp_log_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to enable BGP logging for the VPN connection. Default value is <code>False</code>.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    bgp_log_group_arn: NotRequired[
        "capo_ec2.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch log group where BGP logs will be sent.</p>"""
    bgp_log_output_format: NotRequired["capo_ec2.types.string.String"]
    """<p>The desired output format for BGP logs to be sent to CloudWatch. Default format is <code>json</code>.</p> <p>Valid values: <code>json</code> | <code>text</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CloudWatchLogOptionsSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "log_enabled" in value:
        pairs.append(
            (f"{prefix}.LogEnabled", "true" if value["log_enabled"] else "false")
        )
    if "log_group_arn" in value:
        pairs.append((f"{prefix}.LogGroupArn", str(value["log_group_arn"])))
    if "log_output_format" in value:
        pairs.append((f"{prefix}.LogOutputFormat", str(value["log_output_format"])))
    if "bgp_log_enabled" in value:
        pairs.append(
            (f"{prefix}.BgpLogEnabled", "true" if value["bgp_log_enabled"] else "false")
        )
    if "bgp_log_group_arn" in value:
        pairs.append((f"{prefix}.BgpLogGroupArn", str(value["bgp_log_group_arn"])))
    if "bgp_log_output_format" in value:
        pairs.append(
            (f"{prefix}.BgpLogOutputFormat", str(value["bgp_log_output_format"]))
        )


def deserialize_ec2_query(el: Element) -> CloudWatchLogOptionsSpecification:
    out: CloudWatchLogOptionsSpecification = {}  # type: ignore[typeddict-item]
    child_log_enabled = el.find("LogEnabled")
    if child_log_enabled is not None:
        out["log_enabled"] = (child_log_enabled.text or "").lower() == "true"
    child_log_group_arn = el.find("LogGroupArn")
    if child_log_group_arn is not None:
        out["log_group_arn"] = str(child_log_group_arn.text or "")
    child_log_output_format = el.find("LogOutputFormat")
    if child_log_output_format is not None:
        out["log_output_format"] = str(child_log_output_format.text or "")
    child_bgp_log_enabled = el.find("BgpLogEnabled")
    if child_bgp_log_enabled is not None:
        out["bgp_log_enabled"] = (child_bgp_log_enabled.text or "").lower() == "true"
    child_bgp_log_group_arn = el.find("BgpLogGroupArn")
    if child_bgp_log_group_arn is not None:
        out["bgp_log_group_arn"] = str(child_bgp_log_group_arn.text or "")
    child_bgp_log_output_format = el.find("BgpLogOutputFormat")
    if child_bgp_log_output_format is not None:
        out["bgp_log_output_format"] = str(child_bgp_log_output_format.text or "")
    return out
