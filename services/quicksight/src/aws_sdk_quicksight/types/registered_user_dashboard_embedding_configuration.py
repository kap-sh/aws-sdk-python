"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserDashboardEmbeddingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.registered_user_dashboard_feature_configurations
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class RegisteredUserDashboardEmbeddingConfiguration(TypedDict):
    initial_dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The dashboard ID for the dashboard that you want the user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon Quick Sight renders this dashboard if the user has permissions to view it.</p> <p>If the user does not have permission to view this dashboard, they see a permissions error message.</p>"""
    feature_configurations: NotRequired[
        "aws_sdk_quicksight.types.registered_user_dashboard_feature_configurations.RegisteredUserDashboardFeatureConfigurations"
    ]
    """<p>The feature configurations of an embbedded Amazon Quick Sight dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserDashboardEmbeddingConfiguration) -> dict:
    out: dict = {}
    out["InitialDashboardId"] = value["initial_dashboard_id"]
    if "feature_configurations" in value:
        import aws_sdk_quicksight.types.registered_user_dashboard_feature_configurations

        out["FeatureConfigurations"] = (
            aws_sdk_quicksight.types.registered_user_dashboard_feature_configurations.serialize_json(
                value["feature_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisteredUserDashboardEmbeddingConfiguration:
    out: RegisteredUserDashboardEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if "InitialDashboardId" in data:
        out["initial_dashboard_id"] = data["InitialDashboardId"]
    else:
        raise DeserializationError(
            "RegisteredUserDashboardEmbeddingConfiguration.initial_dashboard_id required"
        )
    if "FeatureConfigurations" in data:
        import aws_sdk_quicksight.types.registered_user_dashboard_feature_configurations

        out["feature_configurations"] = (
            aws_sdk_quicksight.types.registered_user_dashboard_feature_configurations.deserialize_json(
                data["FeatureConfigurations"]
            )
        )
    return out
