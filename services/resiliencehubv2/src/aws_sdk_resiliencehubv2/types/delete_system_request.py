"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteSystemRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn


class DeleteSystemRequest(TypedDict):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSystemRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    return out


def deserialize_json(data: dict) -> DeleteSystemRequest:
    out: DeleteSystemRequest = {}  # type: ignore[typeddict-item]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("DeleteSystemRequest.system_arn required")
    return out
