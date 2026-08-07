"""Generated from Smithy shape ``com.amazonaws.elasticache#CloudWatchLogsDestinationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class CloudWatchLogsDestinationDetails(TypedDict, closed=True):
    log_group: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the CloudWatch Logs log group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudWatchLogsDestinationDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "log_group" in value:
        pairs.append((f"{key_prefix}LogGroup", str(value["log_group"])))


def deserialize_query(el: Element) -> CloudWatchLogsDestinationDetails:
    out: CloudWatchLogsDestinationDetails = {}  # type: ignore[typeddict-item]
    child_log_group = el.find("LogGroup")
    if child_log_group is not None:
        out["log_group"] = str(child_log_group.text or "")
    return out
