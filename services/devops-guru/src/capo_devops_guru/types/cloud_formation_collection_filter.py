"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudFormationCollectionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.stack_names


class CloudFormationCollectionFilter(TypedDict, closed=True):
    stack_names: NotRequired["capo_devops_guru.types.stack_names.StackNames"]
    """<p> An array of CloudFormation stack names. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationCollectionFilter) -> dict:
    out: dict = {}
    if "stack_names" in value:
        import capo_devops_guru.types.stack_names

        out["StackNames"] = capo_devops_guru.types.stack_names.serialize_json(
            value["stack_names"]
        )
    return out


def deserialize_json(data: dict) -> CloudFormationCollectionFilter:
    out: CloudFormationCollectionFilter = {}  # type: ignore[typeddict-item]
    if "StackNames" in data:
        import capo_devops_guru.types.stack_names

        out["stack_names"] = capo_devops_guru.types.stack_names.deserialize_json(
            data["StackNames"]
        )
    return out
