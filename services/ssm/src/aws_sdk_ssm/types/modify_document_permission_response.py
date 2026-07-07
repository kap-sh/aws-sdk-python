"""Generated from Smithy shape ``com.amazonaws.ssm#ModifyDocumentPermissionResponse``."""

from typing_extensions import TypedDict


class ModifyDocumentPermissionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDocumentPermissionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDocumentPermissionResponse:
    out: ModifyDocumentPermissionResponse = {}  # type: ignore[typeddict-item]
    return out
