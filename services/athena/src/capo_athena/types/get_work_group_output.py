"""Generated from Smithy shape ``com.amazonaws.athena#GetWorkGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.work_group


class GetWorkGroupOutput(TypedDict, closed=True):
    work_group: NotRequired["capo_athena.types.work_group.WorkGroup"]
    """<p>Information about the workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkGroupOutput) -> dict:
    out: dict = {}
    if "work_group" in value:
        import capo_athena.types.work_group

        out["WorkGroup"] = capo_athena.types.work_group.serialize_aws_json_1_1(
            value["work_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkGroupOutput:
    out: GetWorkGroupOutput = {}  # type: ignore[typeddict-item]
    if "WorkGroup" in data:
        import capo_athena.types.work_group

        out["work_group"] = capo_athena.types.work_group.deserialize_aws_json_1_1(
            data["WorkGroup"]
        )
    return out
