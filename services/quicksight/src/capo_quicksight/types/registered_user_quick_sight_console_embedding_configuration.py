"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserQuickSightConsoleEmbeddingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.entry_path
    import capo_quicksight.types.registered_user_console_feature_configurations


class RegisteredUserQuickSightConsoleEmbeddingConfiguration(TypedDict, closed=True):
    initial_path: NotRequired["capo_quicksight.types.entry_path.EntryPath"]
    """<p>The initial URL path for the Amazon Quick Sight console. <code>InitialPath</code> is required.</p> <p>The entry point URL is constrained to the following paths:</p> <ul> <li> <p> <code>/start</code> </p> </li> <li> <p> <code>/start/analyses</code> </p> </li> <li> <p> <code>/start/dashboards</code> </p> </li> <li> <p> <code>/start/favorites</code> </p> </li> <li> <p> <code>/dashboards/DashboardId</code>. <i>DashboardId</i> is the actual ID key from the Amazon Quick Sight console URL of the dashboard.</p> </li> <li> <p> <code>/analyses/AnalysisId</code>. <i>AnalysisId</i> is the actual ID key from the Amazon Quick Sight console URL of the analysis.</p> </li> </ul>"""
    feature_configurations: NotRequired[
        "capo_quicksight.types.registered_user_console_feature_configurations.RegisteredUserConsoleFeatureConfigurations"
    ]
    """<p>The embedding configuration of an embedded Amazon Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: RegisteredUserQuickSightConsoleEmbeddingConfiguration,
) -> dict:
    out: dict = {}
    if "initial_path" in value:
        out["InitialPath"] = value["initial_path"]
    if "feature_configurations" in value:
        import capo_quicksight.types.registered_user_console_feature_configurations

        out["FeatureConfigurations"] = (
            capo_quicksight.types.registered_user_console_feature_configurations.serialize_json(
                value["feature_configurations"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> RegisteredUserQuickSightConsoleEmbeddingConfiguration:
    out: RegisteredUserQuickSightConsoleEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if "InitialPath" in data:
        out["initial_path"] = data["InitialPath"]
    if "FeatureConfigurations" in data:
        import capo_quicksight.types.registered_user_console_feature_configurations

        out["feature_configurations"] = (
            capo_quicksight.types.registered_user_console_feature_configurations.deserialize_json(
                data["FeatureConfigurations"]
            )
        )
    return out
