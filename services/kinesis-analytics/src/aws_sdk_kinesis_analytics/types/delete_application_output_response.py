"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#DeleteApplicationOutputResponse``."""

from typing_extensions import TypedDict


class DeleteApplicationOutputResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationOutputResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationOutputResponse:
    out: DeleteApplicationOutputResponse = {}  # type: ignore[typeddict-item]
    return out
