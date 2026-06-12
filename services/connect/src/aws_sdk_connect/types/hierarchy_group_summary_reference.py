"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroupSummaryReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.hierarchy_group_id


class HierarchyGroupSummaryReference(TypedDict):
    id: NotRequired["aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"]
    """<p>The unique identifier for the hierarchy group.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the hierarchy group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroupSummaryReference) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> HierarchyGroupSummaryReference:
    out: HierarchyGroupSummaryReference = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
