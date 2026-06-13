"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateSystemRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_description


class UpdateSystemRequest(TypedDict):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    sharing_enabled: NotRequired["bool"]
    """<p>Whether cross-account sharing is enabled for the system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSystemRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "sharing_enabled" in value:
        out["sharingEnabled"] = value["sharing_enabled"]
    return out


def deserialize_json(data: dict) -> UpdateSystemRequest:
    out: UpdateSystemRequest = {}  # type: ignore[typeddict-item]
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("UpdateSystemRequest.system_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "sharingEnabled" in data:
        out["sharing_enabled"] = data["sharingEnabled"]
    return out
