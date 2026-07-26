"""Generated from Smithy shape ``com.amazonaws.memorydb#MultiRegionParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class MultiRegionParameterGroup(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-region parameter group.</p>"""
    family: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the parameter group family that this multi-region parameter group is compatible with.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A description of the multi-region parameter group.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the multi-region parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionParameterGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "family" in value:
        out["Family"] = value["family"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiRegionParameterGroup:
    out: MultiRegionParameterGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Family" in data:
        out["family"] = data["Family"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    return out
