"""Generated from Smithy shape ``com.amazonaws.mturk#GetQualificationTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.entity_id


class GetQualificationTypeRequest(TypedDict):
    qualification_type_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p>The ID of the QualificationType.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQualificationTypeRequest) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQualificationTypeRequest:
    out: GetQualificationTypeRequest = {}  # type: ignore[typeddict-item]
    if "QualificationTypeId" in data:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        raise DeserializationError(
            "GetQualificationTypeRequest.qualification_type_id required"
        )
    return out
