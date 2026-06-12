"""Generated from Smithy shape ``com.amazonaws.athena#GetWorkGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.work_group


class GetWorkGroupOutput(TypedDict):
    work_group: NotRequired["aws_sdk_athena.types.work_group.WorkGroup"]
    """<p>Information about the workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkGroupOutput) -> dict:
    out: dict = {}
    if "work_group" in value:
        import aws_sdk_athena.types.work_group

        out["WorkGroup"] = aws_sdk_athena.types.work_group.serialize_aws_json_1_1(
            value["work_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkGroupOutput:
    out: GetWorkGroupOutput = {}  # type: ignore[typeddict-item]
    if "WorkGroup" in data:
        import aws_sdk_athena.types.work_group

        out["work_group"] = aws_sdk_athena.types.work_group.deserialize_aws_json_1_1(
            data["WorkGroup"]
        )
    return out
