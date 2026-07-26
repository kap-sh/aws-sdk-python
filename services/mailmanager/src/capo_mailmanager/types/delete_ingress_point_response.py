"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteIngressPointResponse``."""

from typing_extensions import TypedDict


class DeleteIngressPointResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteIngressPointResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteIngressPointResponse:
    out: DeleteIngressPointResponse = {}  # type: ignore[typeddict-item]
    return out
