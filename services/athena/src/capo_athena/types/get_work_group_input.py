"""Generated from Smithy shape ``com.amazonaws.athena#GetWorkGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.work_group_name


class GetWorkGroupInput(TypedDict, closed=True):
    work_group: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The name of the workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkGroupInput) -> dict:
    out: dict = {}
    out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkGroupInput:
    out: GetWorkGroupInput = {}  # type: ignore[typeddict-item]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    else:
        raise DeserializationError("GetWorkGroupInput.work_group required")
    return out
