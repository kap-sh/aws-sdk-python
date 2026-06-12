"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateCloudFormationCollectionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.update_stack_names


class UpdateCloudFormationCollectionFilter(TypedDict):
    stack_names: NotRequired[
        "aws_sdk_devops_guru.types.update_stack_names.UpdateStackNames"
    ]
    """<p> An array of the names of the Amazon Web Services CloudFormation stacks to update. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCloudFormationCollectionFilter) -> dict:
    out: dict = {}
    if "stack_names" in value:
        import aws_sdk_devops_guru.types.update_stack_names

        out["StackNames"] = aws_sdk_devops_guru.types.update_stack_names.serialize_json(
            value["stack_names"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCloudFormationCollectionFilter:
    out: UpdateCloudFormationCollectionFilter = {}  # type: ignore[typeddict-item]
    if "StackNames" in data:
        import aws_sdk_devops_guru.types.update_stack_names

        out["stack_names"] = (
            aws_sdk_devops_guru.types.update_stack_names.deserialize_json(
                data["StackNames"]
            )
        )
    return out
