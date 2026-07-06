"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeleteNamespaceRequest``."""

from typing_extensions import TypedDict


class DeleteNamespaceRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamespaceRequest:
    out: DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
