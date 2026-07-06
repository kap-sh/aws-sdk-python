"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#Identity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.resource_name


class Identity(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN in an Identity.</p>"""
    name: NotRequired["aws_sdk_chime_sdk_identity.types.resource_name.ResourceName"]
    """<p>The name in an Identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Identity) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Identity:
    out: Identity = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
