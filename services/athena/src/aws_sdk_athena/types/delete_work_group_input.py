"""Generated from Smithy shape ``com.amazonaws.athena#DeleteWorkGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.boxed_boolean
    import aws_sdk_athena.types.work_group_name


class DeleteWorkGroupInput(TypedDict, closed=True):
    work_group: "aws_sdk_athena.types.work_group_name.WorkGroupName"
    """<p>The unique name of the workgroup to delete.</p>"""
    recursive_delete_option: NotRequired[
        "aws_sdk_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>The option to delete the workgroup and its contents even if the workgroup contains any named queries, query executions, or notebooks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkGroupInput) -> dict:
    out: dict = {}
    out["WorkGroup"] = value["work_group"]
    if "recursive_delete_option" in value:
        out["RecursiveDeleteOption"] = value["recursive_delete_option"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkGroupInput:
    out: DeleteWorkGroupInput = {}  # type: ignore[typeddict-item]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    else:
        raise DeserializationError("DeleteWorkGroupInput.work_group required")
    if "RecursiveDeleteOption" in data:
        out["recursive_delete_option"] = data["RecursiveDeleteOption"]
    return out
