"""Generated from Smithy shape ``com.amazonaws.route53profiles#DisassociateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.profile_association


class DisassociateProfileResponse(TypedDict, closed=True):
    profile_association: NotRequired[
        "aws_sdk_route53profiles.types.profile_association.ProfileAssociation"
    ]
    """<p> Information about the <code>DisassociateProfile</code> request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateProfileResponse) -> dict:
    out: dict = {}
    if "profile_association" in value:
        import aws_sdk_route53profiles.types.profile_association

        out["ProfileAssociation"] = (
            aws_sdk_route53profiles.types.profile_association.serialize_json(
                value["profile_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateProfileResponse:
    out: DisassociateProfileResponse = {}  # type: ignore[typeddict-item]
    if "ProfileAssociation" in data:
        import aws_sdk_route53profiles.types.profile_association

        out["profile_association"] = (
            aws_sdk_route53profiles.types.profile_association.deserialize_json(
                data["ProfileAssociation"]
            )
        )
    return out
