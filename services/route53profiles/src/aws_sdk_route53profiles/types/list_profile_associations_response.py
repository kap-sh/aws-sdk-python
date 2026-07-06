"""Generated from Smithy shape ``com.amazonaws.route53profiles#ListProfileAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.next_token
    import aws_sdk_route53profiles.types.profile_associations


class ListProfileAssociationsResponse(TypedDict, closed=True):
    profile_associations: NotRequired[
        "aws_sdk_route53profiles.types.profile_associations.ProfileAssociations"
    ]
    """<p> A complex type that containts settings information about the profile's VPC associations. </p>"""
    next_token: NotRequired["aws_sdk_route53profiles.types.next_token.NextToken"]
    """<p> If more than <code>MaxResults</code> profile associations match the specified criteria, you can submit another <code>ListProfileAssociations</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileAssociationsResponse) -> dict:
    out: dict = {}
    if "profile_associations" in value:
        import aws_sdk_route53profiles.types.profile_associations

        out["ProfileAssociations"] = (
            aws_sdk_route53profiles.types.profile_associations.serialize_json(
                value["profile_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileAssociationsResponse:
    out: ListProfileAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "ProfileAssociations" in data:
        import aws_sdk_route53profiles.types.profile_associations

        out["profile_associations"] = (
            aws_sdk_route53profiles.types.profile_associations.deserialize_json(
                data["ProfileAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
