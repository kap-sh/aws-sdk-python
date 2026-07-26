"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.work_group_names_list


class CapacityAssignment(TypedDict, closed=True):
    work_group_names: NotRequired[
        "capo_athena.types.work_group_names_list.WorkGroupNamesList"
    ]
    """<p>The list of workgroup names for the capacity assignment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAssignment) -> dict:
    out: dict = {}
    if "work_group_names" in value:
        import capo_athena.types.work_group_names_list

        out["WorkGroupNames"] = (
            capo_athena.types.work_group_names_list.serialize_aws_json_1_1(
                value["work_group_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityAssignment:
    out: CapacityAssignment = {}  # type: ignore[typeddict-item]
    if "WorkGroupNames" in data:
        import capo_athena.types.work_group_names_list

        out["work_group_names"] = (
            capo_athena.types.work_group_names_list.deserialize_aws_json_1_1(
                data["WorkGroupNames"]
            )
        )
    return out
