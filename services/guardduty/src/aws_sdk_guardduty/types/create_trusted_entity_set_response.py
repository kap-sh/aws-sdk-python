"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateTrustedEntitySetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class CreateTrustedEntitySetResponse(TypedDict):
    trusted_entity_set_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID returned by GuardDuty after creation of the trusted entity set resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrustedEntitySetResponse) -> dict:
    out: dict = {}
    if "trusted_entity_set_id" in value:
        out["trustedEntitySetId"] = value["trusted_entity_set_id"]
    return out


def deserialize_json(data: dict) -> CreateTrustedEntitySetResponse:
    out: CreateTrustedEntitySetResponse = {}  # type: ignore[typeddict-item]
    if "trustedEntitySetId" in data:
        out["trusted_entity_set_id"] = data["trustedEntitySetId"]
    return out
