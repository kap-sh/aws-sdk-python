"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeEventCategoriesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DescribeEventCategoriesMessage(TypedDict, closed=True):
    source_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The source type, such as cluster or parameter group, to which the described event categories apply.</p> <p>Valid values: cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, and scheduled-action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventCategoriesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_type" in value:
        pairs.append((f"{key_prefix}SourceType", str(value["source_type"])))


def deserialize_query(el: Element) -> DescribeEventCategoriesMessage:
    out: DescribeEventCategoriesMessage = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        out["source_type"] = str(child_source_type.text or "")
    return out
