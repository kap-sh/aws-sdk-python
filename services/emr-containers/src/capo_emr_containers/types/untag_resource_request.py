"""Generated from Smithy shape ``com.amazonaws.emrcontainers#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.rsi_arn
    import capo_emr_containers.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_emr_containers.types.rsi_arn.RsiArn"
    """<p>The ARN of resources.</p>"""
    tag_keys: "capo_emr_containers.types.tag_key_list.TagKeyList"
    """<p>The tag keys of the resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
