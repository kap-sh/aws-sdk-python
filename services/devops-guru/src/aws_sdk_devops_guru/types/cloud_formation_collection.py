"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudFormationCollection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.stack_names


class CloudFormationCollection(TypedDict, closed=True):
    stack_names: NotRequired["aws_sdk_devops_guru.types.stack_names.StackNames"]
    """<p> An array of CloudFormation stack names. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationCollection) -> dict:
    out: dict = {}
    if "stack_names" in value:
        import aws_sdk_devops_guru.types.stack_names

        out["StackNames"] = aws_sdk_devops_guru.types.stack_names.serialize_json(
            value["stack_names"]
        )
    return out


def deserialize_json(data: dict) -> CloudFormationCollection:
    out: CloudFormationCollection = {}  # type: ignore[typeddict-item]
    if "StackNames" in data:
        import aws_sdk_devops_guru.types.stack_names

        out["stack_names"] = aws_sdk_devops_guru.types.stack_names.deserialize_json(
            data["StackNames"]
        )
    return out
