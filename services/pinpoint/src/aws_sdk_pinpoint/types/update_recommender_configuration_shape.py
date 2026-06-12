"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateRecommenderConfigurationShape``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of__string


class UpdateRecommenderConfigurationShape(TypedDict):
    attributes: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map of key-value pairs that defines 1-10 custom endpoint or user attributes, depending on the value for the RecommendationProviderIdType property. Each of these attributes temporarily stores a recommended item that's retrieved from the recommender model and sent to an AWS Lambda function for additional processing. Each attribute can be used as a message variable in a message template.</p> <p>In the map, the key is the name of a custom attribute and the value is a custom display name for that attribute. The display name appears in the <b>Attribute finder</b> of the template editor on the Amazon Pinpoint console. The following restrictions apply to these names:</p> <ul><li><p>An attribute name must start with a letter or number and it can contain up to 50 characters. The characters can be letters, numbers, underscores (_), or hyphens (-). Attribute names are case sensitive and must be unique.</p></li> <li><p>An attribute display name must start with a letter or number and it can contain up to 25 characters. The characters can be letters, numbers, spaces, underscores (_), or hyphens (-).</p></li></ul> <p>This object is required if the configuration invokes an AWS Lambda function (RecommendationTransformerUri) to process recommendation data. Otherwise, don't include this object in your request.</p>"""
    description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A custom description of the configuration for the recommender model. The description can contain up to 128 characters. The characters can be letters, numbers, spaces, or the following symbols: _ ; () , ‐.</p>"""
    name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>A custom name of the configuration for the recommender model. The name must start with a letter or number and it can contain up to 128 characters. The characters can be letters, numbers, spaces, underscores (_), or hyphens (-).</p>"""
    recommendation_provider_id_type: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The type of Amazon Pinpoint ID to associate with unique user IDs in the recommender model. This value enables the model to use attribute and event data that’s specific to a particular endpoint or user in an Amazon Pinpoint application. Valid values are:</p> <ul><li><p>PINPOINT_ENDPOINT_ID - Associate each user in the model with a particular endpoint in Amazon Pinpoint. The data is correlated based on endpoint IDs in Amazon Pinpoint. This is the default value.</p></li> <li><p>PINPOINT_USER_ID - Associate each user in the model with a particular user and endpoint in Amazon Pinpoint. The data is correlated based on user IDs in Amazon Pinpoint. If you specify this value, an endpoint definition in Amazon Pinpoint has to specify both a user ID (UserId) and an endpoint ID. Otherwise, messages won’t be sent to the user's endpoint.</p></li></ul>"""
    recommendation_provider_role_arn: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to retrieve recommendation data from the recommender model.</p>"""
    recommendation_provider_uri: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the recommender model to retrieve recommendation data from. This value must match the ARN of an Amazon Personalize campaign.</p>"""
    recommendation_transformer_uri: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the AWS Lambda function to invoke for additional processing of recommendation data that's retrieved from the recommender model.</p>"""
    recommendations_display_name: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>A custom display name for the standard endpoint or user attribute (RecommendationItems) that temporarily stores recommended items for each endpoint or user, depending on the value for the RecommendationProviderIdType property. This value is required if the configuration doesn't invoke an AWS Lambda function (RecommendationTransformerUri) to perform additional processing of recommendation data.</p> <p>This name appears in the <b>Attribute finder</b> of the template editor on the Amazon Pinpoint console. The name can contain up to 25 characters. The characters can be letters, numbers, spaces, underscores (_), or hyphens (-). These restrictions don't apply to attribute values.</p>"""
    recommendations_per_message: NotRequired[
        "aws_sdk_pinpoint.types.__integer.__integer"
    ]
    """<p>The number of recommended items to retrieve from the model for each endpoint or user, depending on the value for the RecommendationProviderIdType property. This number determines how many recommended items are available for use in message variables. The minimum value is 1. The maximum value is 5. The default value is 5.</p> <p>To use multiple recommended items and custom attributes with message variables, you have to use an AWS Lambda function (RecommendationTransformerUri) to perform additional processing of recommendation data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderConfigurationShape) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["Attributes"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["attributes"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "recommendation_provider_id_type" in value:
        out["RecommendationProviderIdType"] = value["recommendation_provider_id_type"]
    if "recommendation_provider_role_arn" in value:
        out["RecommendationProviderRoleArn"] = value["recommendation_provider_role_arn"]
    if "recommendation_provider_uri" in value:
        out["RecommendationProviderUri"] = value["recommendation_provider_uri"]
    if "recommendation_transformer_uri" in value:
        out["RecommendationTransformerUri"] = value["recommendation_transformer_uri"]
    if "recommendations_display_name" in value:
        out["RecommendationsDisplayName"] = value["recommendations_display_name"]
    if "recommendations_per_message" in value:
        out["RecommendationsPerMessage"] = value["recommendations_per_message"]
    return out


def deserialize_json(data: dict) -> UpdateRecommenderConfigurationShape:
    out: UpdateRecommenderConfigurationShape = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["attributes"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["Attributes"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RecommendationProviderIdType" in data:
        out["recommendation_provider_id_type"] = data["RecommendationProviderIdType"]
    if "RecommendationProviderRoleArn" in data:
        out["recommendation_provider_role_arn"] = data["RecommendationProviderRoleArn"]
    if "RecommendationProviderUri" in data:
        out["recommendation_provider_uri"] = data["RecommendationProviderUri"]
    if "RecommendationTransformerUri" in data:
        out["recommendation_transformer_uri"] = data["RecommendationTransformerUri"]
    if "RecommendationsDisplayName" in data:
        out["recommendations_display_name"] = data["RecommendationsDisplayName"]
    if "RecommendationsPerMessage" in data:
        out["recommendations_per_message"] = data["RecommendationsPerMessage"]
    return out
