"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionLogOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ConnectionLogOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether connection logging is enabled.</p>"""
    cloudwatch_log_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the CloudWatch Logs log group. Required if connection logging is enabled.</p>"""
    cloudwatch_log_stream: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the CloudWatch Logs log stream to which the connection data is published.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConnectionLogOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "cloudwatch_log_group" in value:
        pairs.append(
            (f"{prefix}.CloudwatchLogGroup", str(value["cloudwatch_log_group"]))
        )
    if "cloudwatch_log_stream" in value:
        pairs.append(
            (f"{prefix}.CloudwatchLogStream", str(value["cloudwatch_log_stream"]))
        )


def deserialize_ec2_query(el: Element) -> ConnectionLogOptions:
    out: ConnectionLogOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_cloudwatch_log_group = el.find("CloudwatchLogGroup")
    if child_cloudwatch_log_group is not None:
        out["cloudwatch_log_group"] = str(child_cloudwatch_log_group.text or "")
    child_cloudwatch_log_stream = el.find("CloudwatchLogStream")
    if child_cloudwatch_log_stream is not None:
        out["cloudwatch_log_stream"] = str(child_cloudwatch_log_stream.text or "")
    return out
