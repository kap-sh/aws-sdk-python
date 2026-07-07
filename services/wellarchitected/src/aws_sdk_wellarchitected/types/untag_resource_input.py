"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.tag_key_list
    import aws_sdk_wellarchitected.types.workload_arn


class UntagResourceInput(TypedDict, closed=True):
    workload_arn: "aws_sdk_wellarchitected.types.workload_arn.WorkloadArn"
    tag_keys: NotRequired["aws_sdk_wellarchitected.types.tag_key_list.TagKeyList"]
    """<p>A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
