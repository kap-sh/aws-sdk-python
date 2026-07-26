"""Generated from Smithy shape ``com.amazonaws.personalize#FeatureTransformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.featurization_parameters
    import capo_personalize.types.name
    import capo_personalize.types.status


class FeatureTransformation(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the feature transformation.</p>"""
    feature_transformation_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the FeatureTransformation object.</p>"""
    default_parameters: NotRequired[
        "capo_personalize.types.featurization_parameters.FeaturizationParameters"
    ]
    """<p>Provides the default parameters for feature transformation.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the feature transformation.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The last update date and time (in Unix time) of the feature transformation.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the feature transformation.</p> <p>A feature transformation can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureTransformation) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "feature_transformation_arn" in value:
        out["featureTransformationArn"] = value["feature_transformation_arn"]
    if "default_parameters" in value:
        import capo_personalize.types.featurization_parameters

        out["defaultParameters"] = (
            capo_personalize.types.featurization_parameters.serialize_aws_json_1_1(
                value["default_parameters"]
            )
        )
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureTransformation:
    out: FeatureTransformation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "featureTransformationArn" in data:
        out["feature_transformation_arn"] = data["featureTransformationArn"]
    if "defaultParameters" in data:
        import capo_personalize.types.featurization_parameters

        out["default_parameters"] = (
            capo_personalize.types.featurization_parameters.deserialize_aws_json_1_1(
                data["defaultParameters"]
            )
        )
    if "creationDateTime" in data:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    return out
