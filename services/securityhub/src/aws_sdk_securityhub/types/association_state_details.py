"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationStateDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AssociationStateDetails(TypedDict):
    state: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The state of the association. </p>"""
    status_message: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The status message, if applicable. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociationStateDetails) -> dict:
    out: dict = {}
    if "state" in value:
        out["State"] = value["state"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> AssociationStateDetails:
    out: AssociationStateDetails = {}  # type: ignore[typeddict-item]
    if "State" in data:
        out["state"] = data["State"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
