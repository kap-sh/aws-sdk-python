"""Generated from Smithy shape ``com.amazonaws.repostspace#UpdateSpaceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.arn
    import aws_sdk_repostspace.types.space_description
    import aws_sdk_repostspace.types.space_id
    import aws_sdk_repostspace.types.supported_email_domains_parameters
    import aws_sdk_repostspace.types.tier_level


class UpdateSpaceInput(TypedDict):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of this private re:Post.</p>"""
    description: NotRequired[
        "aws_sdk_repostspace.types.space_description.SpaceDescription"
    ]
    """<p>A description for the private re:Post. This is used only to help you identify this private re:Post.</p>"""
    tier: NotRequired["aws_sdk_repostspace.types.tier_level.TierLevel"]
    """<p>The pricing tier of this private re:Post.</p>"""
    role_arn: NotRequired["aws_sdk_repostspace.types.arn.Arn"]
    """<p>The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.</p>"""
    supported_email_domains: NotRequired[
        "aws_sdk_repostspace.types.supported_email_domains_parameters.SupportedEmailDomainsParameters"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tier" in value:
        import aws_sdk_repostspace.types.tier_level

        out["tier"] = aws_sdk_repostspace.types.tier_level.serialize_json(value["tier"])
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "supported_email_domains" in value:
        import aws_sdk_repostspace.types.supported_email_domains_parameters

        out["supportedEmailDomains"] = (
            aws_sdk_repostspace.types.supported_email_domains_parameters.serialize_json(
                value["supported_email_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSpaceInput:
    out: UpdateSpaceInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "tier" in data:
        import aws_sdk_repostspace.types.tier_level

        out["tier"] = aws_sdk_repostspace.types.tier_level.deserialize_json(
            data["tier"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "supportedEmailDomains" in data:
        import aws_sdk_repostspace.types.supported_email_domains_parameters

        out["supported_email_domains"] = (
            aws_sdk_repostspace.types.supported_email_domains_parameters.deserialize_json(
                data["supportedEmailDomains"]
            )
        )
    return out
