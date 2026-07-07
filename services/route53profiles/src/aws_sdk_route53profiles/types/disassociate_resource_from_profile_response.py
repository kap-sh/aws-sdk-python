"""Generated from Smithy shape ``com.amazonaws.route53profiles#DisassociateResourceFromProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.profile_resource_association


class DisassociateResourceFromProfileResponse(TypedDict, closed=True):
    profile_resource_association: NotRequired[
        "aws_sdk_route53profiles.types.profile_resource_association.ProfileResourceAssociation"
    ]
    """<p> Information about the <code>DisassociateResourceFromProfile</code> request, including the status of the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceFromProfileResponse) -> dict:
    out: dict = {}
    if "profile_resource_association" in value:
        import aws_sdk_route53profiles.types.profile_resource_association

        out["ProfileResourceAssociation"] = (
            aws_sdk_route53profiles.types.profile_resource_association.serialize_json(
                value["profile_resource_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateResourceFromProfileResponse:
    out: DisassociateResourceFromProfileResponse = {}  # type: ignore[typeddict-item]
    if "ProfileResourceAssociation" in data:
        import aws_sdk_route53profiles.types.profile_resource_association

        out["profile_resource_association"] = (
            aws_sdk_route53profiles.types.profile_resource_association.deserialize_json(
                data["ProfileResourceAssociation"]
            )
        )
    return out
