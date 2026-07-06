"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogCloudWatchLogsDestinationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class VerifiedAccessLogCloudWatchLogsDestinationOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    log_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the CloudWatch Logs log group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessLogCloudWatchLogsDestinationOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "log_group" in value:
        pairs.append((f"{prefix}.LogGroup", str(value["log_group"])))


def deserialize_ec2_query(
    el: Element,
) -> VerifiedAccessLogCloudWatchLogsDestinationOptions:
    out: VerifiedAccessLogCloudWatchLogsDestinationOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_log_group = el.find("LogGroup")
    if child_log_group is not None:
        out["log_group"] = str(child_log_group.text or "")
    return out
