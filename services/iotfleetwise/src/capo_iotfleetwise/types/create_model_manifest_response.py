"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateModelManifestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.resource_name


class CreateModelManifestResponse(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the created vehicle model.</p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The ARN of the created vehicle model.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateModelManifestResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateModelManifestResponse:
    out: CreateModelManifestResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateModelManifestResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateModelManifestResponse.arn required")
    return out
