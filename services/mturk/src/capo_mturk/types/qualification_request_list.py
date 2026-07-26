"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.qualification_request

QualificationRequestList: TypeAlias = list[
    "capo_mturk.types.qualification_request.QualificationRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationRequestList) -> list:
    import capo_mturk.types.qualification_request

    out: list = []
    for item in value:
        out.append(capo_mturk.types.qualification_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QualificationRequestList:
    import capo_mturk.types.qualification_request

    out: QualificationRequestList = []
    for item in data:
        out.append(
            capo_mturk.types.qualification_request.deserialize_aws_json_1_1(item)
        )
    return out
