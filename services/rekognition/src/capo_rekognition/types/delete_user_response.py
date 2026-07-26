"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteUserResponse``."""

from typing_extensions import TypedDict


class DeleteUserResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserResponse:
    out: DeleteUserResponse = {}  # type: ignore[typeddict-item]
    return out
