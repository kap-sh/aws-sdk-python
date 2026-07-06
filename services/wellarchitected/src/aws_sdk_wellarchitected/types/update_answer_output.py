"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAnswerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.answer
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.workload_id


class UpdateAnswerOutput(TypedDict, closed=True):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    answer: NotRequired["aws_sdk_wellarchitected.types.answer.Answer"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnswerOutput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "answer" in value:
        import aws_sdk_wellarchitected.types.answer

        out["Answer"] = aws_sdk_wellarchitected.types.answer.serialize_json(
            value["answer"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAnswerOutput:
    out: UpdateAnswerOutput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "Answer" in data:
        import aws_sdk_wellarchitected.types.answer

        out["answer"] = aws_sdk_wellarchitected.types.answer.deserialize_json(
            data["Answer"]
        )
    return out
