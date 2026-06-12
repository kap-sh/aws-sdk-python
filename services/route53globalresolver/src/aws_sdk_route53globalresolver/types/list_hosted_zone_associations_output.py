"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListHostedZoneAssociationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.hosted_zone_associations


class ListHostedZoneAssociationsOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    hosted_zone_associations: "aws_sdk_route53globalresolver.types.hosted_zone_associations.HostedZoneAssociations"
    """<p>List of the private hosted zone associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHostedZoneAssociationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_route53globalresolver.types.hosted_zone_associations

    out["hostedZoneAssociations"] = (
        aws_sdk_route53globalresolver.types.hosted_zone_associations.serialize_json(
            value["hosted_zone_associations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListHostedZoneAssociationsOutput:
    out: ListHostedZoneAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "hostedZoneAssociations" in data:
        import aws_sdk_route53globalresolver.types.hosted_zone_associations

        out["hosted_zone_associations"] = (
            aws_sdk_route53globalresolver.types.hosted_zone_associations.deserialize_json(
                data["hostedZoneAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListHostedZoneAssociationsOutput.hosted_zone_associations required"
        )
    return out
