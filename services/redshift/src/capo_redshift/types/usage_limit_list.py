"""Generated from Smithy shape ``com.amazonaws.redshift#UsageLimitList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.usage_limits


class UsageLimitList(TypedDict, closed=True):
    usage_limits: NotRequired["capo_redshift.types.usage_limits.UsageLimits"]
    """<p>Contains the output from the <a>DescribeUsageLimits</a> action. </p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UsageLimitList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "usage_limits" in value:
        import capo_redshift.types.usage_limits

        capo_redshift.types.usage_limits.serialize_query(
            value["usage_limits"], pairs, f"{key_prefix}UsageLimits"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> UsageLimitList:
    out: UsageLimitList = {}  # type: ignore[typeddict-item]
    child_usage_limits = el.find("UsageLimits")
    if child_usage_limits is not None:
        import capo_redshift.types.usage_limits

        out["usage_limits"] = capo_redshift.types.usage_limits.deserialize_query(
            child_usage_limits
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
