"""Generated from Smithy shape ``com.amazonaws.workmail#PutMailboxPermissionsResponse``."""

from typing_extensions import TypedDict


class PutMailboxPermissionsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutMailboxPermissionsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutMailboxPermissionsResponse:
    out: PutMailboxPermissionsResponse = {}  # type: ignore[typeddict-item]
    return out
