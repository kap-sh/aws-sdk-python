"""Generated from Smithy shape ``com.amazonaws.route53profiles#ListProfileResourceAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.next_token
    import aws_sdk_route53profiles.types.profile_resource_associations


class ListProfileResourceAssociationsResponse(TypedDict, closed=True):
    profile_resource_associations: NotRequired[
        "aws_sdk_route53profiles.types.profile_resource_associations.ProfileResourceAssociations"
    ]
    """<p> Information about the profile resource association that you specified in a <code>GetProfileResourceAssociation</code> request. </p>"""
    next_token: NotRequired["aws_sdk_route53profiles.types.next_token.NextToken"]
    """<p> If more than <code>MaxResults</code> resource associations match the specified criteria, you can submit another <code>ListProfileResourceAssociations</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileResourceAssociationsResponse) -> dict:
    out: dict = {}
    if "profile_resource_associations" in value:
        import aws_sdk_route53profiles.types.profile_resource_associations

        out["ProfileResourceAssociations"] = (
            aws_sdk_route53profiles.types.profile_resource_associations.serialize_json(
                value["profile_resource_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileResourceAssociationsResponse:
    out: ListProfileResourceAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "ProfileResourceAssociations" in data:
        import aws_sdk_route53profiles.types.profile_resource_associations

        out["profile_resource_associations"] = (
            aws_sdk_route53profiles.types.profile_resource_associations.deserialize_json(
                data["ProfileResourceAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
