"""Generated from Smithy shape ``com.amazonaws.mturk#GetAssignmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.assignment
    import aws_sdk_mturk.types.hit


class GetAssignmentResponse(TypedDict, closed=True):
    assignment: NotRequired["aws_sdk_mturk.types.assignment.Assignment"]
    """<p> The assignment. The response includes one Assignment element. </p>"""
    hit: NotRequired["aws_sdk_mturk.types.hit.HIT"]
    """<p> The HIT associated with this assignment. The response includes one HIT element.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAssignmentResponse) -> dict:
    out: dict = {}
    if "assignment" in value:
        import aws_sdk_mturk.types.assignment

        out["Assignment"] = aws_sdk_mturk.types.assignment.serialize_aws_json_1_1(
            value["assignment"]
        )
    if "hit" in value:
        import aws_sdk_mturk.types.hit

        out["HIT"] = aws_sdk_mturk.types.hit.serialize_aws_json_1_1(value["hit"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAssignmentResponse:
    out: GetAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "Assignment" in data:
        import aws_sdk_mturk.types.assignment

        out["assignment"] = aws_sdk_mturk.types.assignment.deserialize_aws_json_1_1(
            data["Assignment"]
        )
    if "HIT" in data:
        import aws_sdk_mturk.types.hit

        out["hit"] = aws_sdk_mturk.types.hit.deserialize_aws_json_1_1(data["HIT"])
    return out
