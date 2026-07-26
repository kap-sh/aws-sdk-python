"""Generated from Smithy shape ``com.amazonaws.mturk#CreateQualificationTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.qualification_type


class CreateQualificationTypeResponse(TypedDict, closed=True):
    qualification_type: NotRequired[
        "capo_mturk.types.qualification_type.QualificationType"
    ]
    """<p>The created Qualification type, returned as a QualificationType data structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateQualificationTypeResponse) -> dict:
    out: dict = {}
    if "qualification_type" in value:
        import capo_mturk.types.qualification_type

        out["QualificationType"] = (
            capo_mturk.types.qualification_type.serialize_aws_json_1_1(
                value["qualification_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateQualificationTypeResponse:
    out: CreateQualificationTypeResponse = {}  # type: ignore[typeddict-item]
    if "QualificationType" in data:
        import capo_mturk.types.qualification_type

        out["qualification_type"] = (
            capo_mturk.types.qualification_type.deserialize_aws_json_1_1(
                data["QualificationType"]
            )
        )
    return out
