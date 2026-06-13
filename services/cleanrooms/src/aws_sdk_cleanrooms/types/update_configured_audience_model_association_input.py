"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredAudienceModelAssociationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_audience_model_association_identifier
    import aws_sdk_cleanrooms.types.configured_audience_model_association_name
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_description


class UpdateConfiguredAudienceModelAssociationInput(TypedDict):
    configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>A unique identifier for the configured audience model association that you want to update.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier of the membership that contains the configured audience model association that you want to update.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A new description for the configured audience model association.</p>"""
    name: NotRequired[
        "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
    ]
    """<p>A new name for the configured audience model association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredAudienceModelAssociationInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateConfiguredAudienceModelAssociationInput:
    out: UpdateConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    return out
