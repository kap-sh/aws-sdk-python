"""Generated from Smithy shape ``com.amazonaws.mturk#GetQualificationTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.qualification_type


class GetQualificationTypeResponse(TypedDict):
    qualification_type: NotRequired[
        "aws_sdk_mturk.types.qualification_type.QualificationType"
    ]
    """<p> The returned Qualification Type</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQualificationTypeResponse) -> dict:
    out: dict = {}
    if "qualification_type" in value:
        import aws_sdk_mturk.types.qualification_type

        out["QualificationType"] = (
            aws_sdk_mturk.types.qualification_type.serialize_aws_json_1_1(
                value["qualification_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQualificationTypeResponse:
    out: GetQualificationTypeResponse = {}  # type: ignore[typeddict-item]
    if "QualificationType" in data:
        import aws_sdk_mturk.types.qualification_type

        out["qualification_type"] = (
            aws_sdk_mturk.types.qualification_type.deserialize_aws_json_1_1(
                data["QualificationType"]
            )
        )
    return out
