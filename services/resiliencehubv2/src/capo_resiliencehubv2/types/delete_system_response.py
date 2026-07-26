"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteSystemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class DeleteSystemResponse(TypedDict, closed=True):
    system_arn: "capo_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSystemResponse) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    return out


def deserialize_json(data: dict) -> DeleteSystemResponse:
    out: DeleteSystemResponse = {}  # type: ignore[typeddict-item]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("DeleteSystemResponse.system_arn required")
    return out
