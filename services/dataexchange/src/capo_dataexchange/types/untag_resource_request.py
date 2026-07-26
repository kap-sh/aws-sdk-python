"""Generated from Smithy shape ``com.amazonaws.dataexchange#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.list_of__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_dataexchange.types.__string.__string"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>"""
    tag_keys: "capo_dataexchange.types.list_of__string.ListOf__string"
    """<p>The key tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
