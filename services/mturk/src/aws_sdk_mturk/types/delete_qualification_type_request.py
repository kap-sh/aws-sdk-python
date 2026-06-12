"""Generated from Smithy shape ``com.amazonaws.mturk#DeleteQualificationTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.entity_id


class DeleteQualificationTypeRequest(TypedDict):
    qualification_type_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p>The ID of the QualificationType to dispose.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteQualificationTypeRequest) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteQualificationTypeRequest:
    out: DeleteQualificationTypeRequest = {}  # type: ignore[typeddict-item]
    if "QualificationTypeId" in data:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        raise DeserializationError(
            "DeleteQualificationTypeRequest.qualification_type_id required"
        )
    return out
