"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteUsageLimitMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteUsageLimitMessage(TypedDict, closed=True):
    usage_limit_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the usage limit to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteUsageLimitMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "usage_limit_id" in value:
        pairs.append((f"{key_prefix}UsageLimitId", str(value["usage_limit_id"])))


def deserialize_query(el: Element) -> DeleteUsageLimitMessage:
    out: DeleteUsageLimitMessage = {}  # type: ignore[typeddict-item]
    child_usage_limit_id = el.find("UsageLimitId")
    if child_usage_limit_id is not None:
        out["usage_limit_id"] = str(child_usage_limit_id.text or "")
    return out
