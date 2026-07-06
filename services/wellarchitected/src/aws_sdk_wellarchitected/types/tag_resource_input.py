"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.tag_map
    import aws_sdk_wellarchitected.types.workload_arn


class TagResourceInput(TypedDict, closed=True):
    workload_arn: "aws_sdk_wellarchitected.types.workload_arn.WorkloadArn"
    tags: NotRequired["aws_sdk_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_wellarchitected.types.tag_map

        out["Tags"] = aws_sdk_wellarchitected.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_wellarchitected.types.tag_map

        out["tags"] = aws_sdk_wellarchitected.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
