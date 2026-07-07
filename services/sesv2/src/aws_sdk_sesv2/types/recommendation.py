"""Generated from Smithy shape ``com.amazonaws.sesv2#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.recommendation_description
    import aws_sdk_sesv2.types.recommendation_impact
    import aws_sdk_sesv2.types.recommendation_status
    import aws_sdk_sesv2.types.recommendation_type
    import aws_sdk_sesv2.types.timestamp


class Recommendation(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The resource affected by the recommendation, with values like <code>arn:aws:ses:us-east-1:123456789012:identity/example.com</code>.</p>"""
    type: NotRequired["aws_sdk_sesv2.types.recommendation_type.RecommendationType"]
    """<p>The recommendation type, with values like <code>DKIM</code>, <code>SPF</code>, <code>DMARC</code>, <code>BIMI</code>, or <code>COMPLAINT</code>.</p>"""
    description: NotRequired[
        "aws_sdk_sesv2.types.recommendation_description.RecommendationDescription"
    ]
    """<p>The recommendation description / disambiguator - e.g. <code>DKIM1</code> and <code>DKIM2</code> are different recommendations about your DKIM setup.</p>"""
    status: NotRequired[
        "aws_sdk_sesv2.types.recommendation_status.RecommendationStatus"
    ]
    """<p>The recommendation status, with values like <code>OPEN</code> or <code>FIXED</code>.</p>"""
    created_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The first time this issue was encountered and the recommendation was generated.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>The last time the recommendation was updated.</p>"""
    impact: NotRequired[
        "aws_sdk_sesv2.types.recommendation_impact.RecommendationImpact"
    ]
    """<p>The recommendation impact, with values like <code>HIGH</code> or <code>LOW</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "type" in value:
        import aws_sdk_sesv2.types.recommendation_type

        out["Type"] = aws_sdk_sesv2.types.recommendation_type.serialize_json(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_sesv2.types.recommendation_status

        out["Status"] = aws_sdk_sesv2.types.recommendation_status.serialize_json(
            value["status"]
        )
    if "created_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["CreatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    if "impact" in value:
        import aws_sdk_sesv2.types.recommendation_impact

        out["Impact"] = aws_sdk_sesv2.types.recommendation_impact.serialize_json(
            value["impact"]
        )
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Type" in data:
        import aws_sdk_sesv2.types.recommendation_type

        out["type"] = aws_sdk_sesv2.types.recommendation_type.deserialize_json(
            data["Type"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_sesv2.types.recommendation_status

        out["status"] = aws_sdk_sesv2.types.recommendation_status.deserialize_json(
            data["Status"]
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["created_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_updated_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    if "Impact" in data:
        import aws_sdk_sesv2.types.recommendation_impact

        out["impact"] = aws_sdk_sesv2.types.recommendation_impact.deserialize_json(
            data["Impact"]
        )
    return out
