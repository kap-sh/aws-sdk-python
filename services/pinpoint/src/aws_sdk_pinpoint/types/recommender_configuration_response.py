"""Generated from Smithy shape ``com.amazonaws.pinpoint#RecommenderConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of__string


class RecommenderConfigurationResponse(TypedDict, closed=True):
    attributes: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A map that defines 1-10 custom endpoint or user attributes, depending on the value for the RecommendationProviderIdType property. Each of these attributes temporarily stores a recommended item that's retrieved from the recommender model and sent to an AWS Lambda function for additional processing. Each attribute can be used as a message variable in a message template.</p> <p>This value is null if the configuration doesn't invoke an AWS Lambda function (RecommendationTransformerUri) to perform additional processing of recommendation data.</p>"""
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in extended ISO 8601 format, when the configuration was created for the recommender model.</p>"""
    description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The custom description of the configuration for the recommender model.</p>"""
    id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the recommender model configuration.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in extended ISO 8601 format, when the configuration for the recommender model was last modified.</p>"""
    name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The custom name of the configuration for the recommender model.</p>"""
    recommendation_provider_id_type: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The type of Amazon Pinpoint ID that's associated with unique user IDs in the recommender model. This value enables the model to use attribute and event data that’s specific to a particular endpoint or user in an Amazon Pinpoint application. Possible values are:</p> <ul><li><p>PINPOINT_ENDPOINT_ID - Each user in the model is associated with a particular endpoint in Amazon Pinpoint. The data is correlated based on endpoint IDs in Amazon Pinpoint. This is the default value.</p></li> <li><p>PINPOINT_USER_ID - Each user in the model is associated with a particular user and endpoint in Amazon Pinpoint. The data is correlated based on user IDs in Amazon Pinpoint. If this value is specified, an endpoint definition in Amazon Pinpoint has to specify both a user ID (UserId) and an endpoint ID. Otherwise, messages won’t be sent to the user's endpoint.</p></li></ul>"""
    recommendation_provider_role_arn: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to retrieve recommendation data from the recommender model.</p>"""
    recommendation_provider_uri: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the recommender model that Amazon Pinpoint retrieves the recommendation data from. This value is the ARN of an Amazon Personalize campaign.</p>"""
    recommendation_transformer_uri: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to perform additional processing of recommendation data that it retrieves from the recommender model.</p>"""
    recommendations_display_name: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The custom display name for the standard endpoint or user attribute (RecommendationItems) that temporarily stores recommended items for each endpoint or user, depending on the value for the RecommendationProviderIdType property. This name appears in the <b>Attribute finder</b> of the template editor on the Amazon Pinpoint console.</p> <p>This value is null if the configuration doesn't invoke an AWS Lambda function (RecommendationTransformerUri) to perform additional processing of recommendation data.</p>"""
    recommendations_per_message: NotRequired[
        "aws_sdk_pinpoint.types.__integer.__integer"
    ]
    """<p>The number of recommended items that are retrieved from the model for each endpoint or user, depending on the value for the RecommendationProviderIdType property. This number determines how many recommended items are available for use in message variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderConfigurationResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["Attributes"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["attributes"]
        )
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "description" in value:
        out["Description"] = value["description"]
    if "id" in value:
        out["Id"] = value["id"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
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


def deserialize_json(data: dict) -> RecommenderConfigurationResponse:
    out: RecommenderConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["attributes"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["Attributes"]
        )
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
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
