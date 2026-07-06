"""Generated from Smithy shape ``com.amazonaws.route53profiles#GetProfileAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.profile_association


class GetProfileAssociationResponse(TypedDict, closed=True):
    profile_association: NotRequired[
        "aws_sdk_route53profiles.types.profile_association.ProfileAssociation"
    ]
    """<p> Information about the Profile association that you specified in a <code>GetProfileAssociation</code> request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileAssociationResponse) -> dict:
    out: dict = {}
    if "profile_association" in value:
        import aws_sdk_route53profiles.types.profile_association

        out["ProfileAssociation"] = (
            aws_sdk_route53profiles.types.profile_association.serialize_json(
                value["profile_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetProfileAssociationResponse:
    out: GetProfileAssociationResponse = {}  # type: ignore[typeddict-item]
    if "ProfileAssociation" in data:
        import aws_sdk_route53profiles.types.profile_association

        out["profile_association"] = (
            aws_sdk_route53profiles.types.profile_association.deserialize_json(
                data["ProfileAssociation"]
            )
        )
    return out
