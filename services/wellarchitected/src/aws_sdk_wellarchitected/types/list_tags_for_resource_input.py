"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    workload_arn: "aws_sdk_wellarchitected.types.workload_arn.WorkloadArn"


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
