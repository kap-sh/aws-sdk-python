"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAssignment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.work_group_names_list


class CapacityAssignment(TypedDict):
    work_group_names: NotRequired[
        "aws_sdk_athena.types.work_group_names_list.WorkGroupNamesList"
    ]
    """<p>The list of workgroup names for the capacity assignment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAssignment) -> dict:
    out: dict = {}
    if "work_group_names" in value:
        import aws_sdk_athena.types.work_group_names_list

        out["WorkGroupNames"] = (
            aws_sdk_athena.types.work_group_names_list.serialize_aws_json_1_1(
                value["work_group_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityAssignment:
    out: CapacityAssignment = {}  # type: ignore[typeddict-item]
    if "WorkGroupNames" in data:
        import aws_sdk_athena.types.work_group_names_list

        out["work_group_names"] = (
            aws_sdk_athena.types.work_group_names_list.deserialize_aws_json_1_1(
                data["WorkGroupNames"]
            )
        )
    return out
