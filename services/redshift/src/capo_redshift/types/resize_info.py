"""Generated from Smithy shape ``com.amazonaws.redshift#ResizeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean
    import capo_redshift.types.string


class ResizeInfo(TypedDict, closed=True):
    resize_type: NotRequired["capo_redshift.types.string.String"]
    """<p>Returns the value <code>ClassicResize</code>.</p>"""
    allow_cancel_resize: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>A boolean value indicating if the resize operation can be cancelled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResizeInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resize_type" in value:
        pairs.append((f"{key_prefix}ResizeType", str(value["resize_type"])))
    if "allow_cancel_resize" in value:
        pairs.append(
            (
                f"{key_prefix}AllowCancelResize",
                "true" if value["allow_cancel_resize"] else "false",
            )
        )


def deserialize_query(el: Element) -> ResizeInfo:
    out: ResizeInfo = {}  # type: ignore[typeddict-item]
    child_resize_type = el.find("ResizeType")
    if child_resize_type is not None:
        out["resize_type"] = str(child_resize_type.text or "")
    child_allow_cancel_resize = el.find("AllowCancelResize")
    if child_allow_cancel_resize is not None:
        out["allow_cancel_resize"] = (
            child_allow_cancel_resize.text or ""
        ).lower() == "true"
    return out
