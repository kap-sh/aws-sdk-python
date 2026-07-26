"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.scan_name_arn
    import capo_codeguru_security.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_codeguru_security.types.scan_name_arn.ScanNameArn"
    """<p>The ARN of the <code>ScanName</code> object. You can retrieve this ARN by calling <code>CreateScan</code>, <code>ListScans</code>, or <code>GetScan</code>.</p>"""
    tag_keys: "capo_codeguru_security.types.tag_key_list.TagKeyList"
    """<p>A list of keys for each tag you want to remove from a scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
