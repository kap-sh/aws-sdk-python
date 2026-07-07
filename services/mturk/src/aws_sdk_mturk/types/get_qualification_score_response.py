"""Generated from Smithy shape ``com.amazonaws.mturk#GetQualificationScoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.qualification


class GetQualificationScoreResponse(TypedDict, closed=True):
    qualification: NotRequired["aws_sdk_mturk.types.qualification.Qualification"]
    """<p> The Qualification data structure of the Qualification assigned to a user, including the Qualification type and the value (score). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQualificationScoreResponse) -> dict:
    out: dict = {}
    if "qualification" in value:
        import aws_sdk_mturk.types.qualification

        out["Qualification"] = aws_sdk_mturk.types.qualification.serialize_aws_json_1_1(
            value["qualification"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQualificationScoreResponse:
    out: GetQualificationScoreResponse = {}  # type: ignore[typeddict-item]
    if "Qualification" in data:
        import aws_sdk_mturk.types.qualification

        out["qualification"] = (
            aws_sdk_mturk.types.qualification.deserialize_aws_json_1_1(
                data["Qualification"]
            )
        )
    return out
