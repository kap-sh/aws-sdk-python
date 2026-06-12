"""Generated from Smithy shape ``com.amazonaws.elasticache#CloudWatchLogsDestinationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class CloudWatchLogsDestinationDetails(TypedDict):
    log_group: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the CloudWatch Logs log group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudWatchLogsDestinationDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "log_group" in value:
        pairs.append((f"{prefix}.LogGroup", str(value["log_group"])))


def deserialize_query(el: Element) -> CloudWatchLogsDestinationDetails:
    out: CloudWatchLogsDestinationDetails = {}  # type: ignore[typeddict-item]
    child_log_group = el.find("LogGroup")
    if child_log_group is not None:
        out["log_group"] = str(child_log_group.text or "")
    return out
