"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.scan_name_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_codeguru_security.types.scan_name_arn.ScanNameArn"
    """<p>The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>CreateScan</code>, <code>ListScans</code>, or <code>GetScan</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
