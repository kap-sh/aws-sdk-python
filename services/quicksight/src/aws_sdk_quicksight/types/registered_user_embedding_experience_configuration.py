"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserEmbeddingExperienceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.registered_user_dashboard_embedding_configuration
    import aws_sdk_quicksight.types.registered_user_dashboard_visual_embedding_configuration
    import aws_sdk_quicksight.types.registered_user_generative_qn_a_embedding_configuration
    import aws_sdk_quicksight.types.registered_user_q_search_bar_embedding_configuration
    import aws_sdk_quicksight.types.registered_user_quick_chat_embedding_configuration
    import aws_sdk_quicksight.types.registered_user_quick_sight_console_embedding_configuration


class RegisteredUserEmbeddingExperienceConfiguration(TypedDict):
    dashboard: NotRequired[
        "aws_sdk_quicksight.types.registered_user_dashboard_embedding_configuration.RegisteredUserDashboardEmbeddingConfiguration"
    ]
    """<p>The configuration details for providing a dashboard embedding experience.</p>"""
    quick_sight_console: NotRequired[
        "aws_sdk_quicksight.types.registered_user_quick_sight_console_embedding_configuration.RegisteredUserQuickSightConsoleEmbeddingConfiguration"
    ]
    r"""<p>The configuration details for providing each Amazon Quick Sight console embedding experience. This can be used along with custom permissions to restrict access to certain features. For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html\">Customizing Access to the Amazon Quick Sight Console</a> in the <i>Amazon Quick User Guide</i>.</p> <p>Use <code> <a href=\"https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html\">GenerateEmbedUrlForRegisteredUser</a> </code> where you want to provide an authoring portal that allows users to create data sources, datasets, analyses, and dashboards. The users who accesses an embedded Amazon Quick Sight console needs to belong to the author or admin security cohort. If you want to restrict permissions to some of these features, add a custom permissions profile to the user with the <code> <a href=\"https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html\">UpdateUser</a> </code> API operation. Use the <code> <a href=\"https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html\">RegisterUser</a> </code> API operation to add a new user with a custom permission profile attached. For more information, see the following sections in the <i>Amazon Quick User Guide</i>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-full-console-for-authenticated-users.html\">Embedding the Full Functionality of the Amazon Quick Sight Console for Authenticated Users</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html\">Customizing Access to the Amazon Quick Console</a> </p> </li> </ul> <p>For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html\">Amazon Quick Developer Portal</a>.</p>"""
    q_search_bar: NotRequired[
        "aws_sdk_quicksight.types.registered_user_q_search_bar_embedding_configuration.RegisteredUserQSearchBarEmbeddingConfiguration"
    ]
    r"""<p>The configuration details for embedding the Q search bar.</p> <p>For more information about embedding the Q search bar, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html\">Embedding Overview</a> in the <i>Amazon Quick Sight User Guide</i>.</p>"""
    dashboard_visual: NotRequired[
        "aws_sdk_quicksight.types.registered_user_dashboard_visual_embedding_configuration.RegisteredUserDashboardVisualEmbeddingConfiguration"
    ]
    """<p>The type of embedding experience. In this case, Amazon Quick Sight visuals.</p>"""
    generative_qn_a: NotRequired[
        "aws_sdk_quicksight.types.registered_user_generative_qn_a_embedding_configuration.RegisteredUserGenerativeQnAEmbeddingConfiguration"
    ]
    r"""<p>The configuration details for embedding the Generative Q&A experience.</p> <p>For more information about embedding the Generative Q&A experience, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html\">Embedding Overview</a> in the <i>Amazon Quick Sight User Guide</i>.</p>"""
    quick_chat: NotRequired[
        "aws_sdk_quicksight.types.registered_user_quick_chat_embedding_configuration.RegisteredUserQuickChatEmbeddingConfiguration"
    ]
    """<p>The configuration details for embedding the Quick chat agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserEmbeddingExperienceConfiguration) -> dict:
    out: dict = {}
    if "dashboard" in value:
        import aws_sdk_quicksight.types.registered_user_dashboard_embedding_configuration

        out["Dashboard"] = (
            aws_sdk_quicksight.types.registered_user_dashboard_embedding_configuration.serialize_json(
                value["dashboard"]
            )
        )
    if "quick_sight_console" in value:
        import aws_sdk_quicksight.types.registered_user_quick_sight_console_embedding_configuration

        out["QuickSightConsole"] = (
            aws_sdk_quicksight.types.registered_user_quick_sight_console_embedding_configuration.serialize_json(
                value["quick_sight_console"]
            )
        )
    if "q_search_bar" in value:
        import aws_sdk_quicksight.types.registered_user_q_search_bar_embedding_configuration

        out["QSearchBar"] = (
            aws_sdk_quicksight.types.registered_user_q_search_bar_embedding_configuration.serialize_json(
                value["q_search_bar"]
            )
        )
    if "dashboard_visual" in value:
        import aws_sdk_quicksight.types.registered_user_dashboard_visual_embedding_configuration

        out["DashboardVisual"] = (
            aws_sdk_quicksight.types.registered_user_dashboard_visual_embedding_configuration.serialize_json(
                value["dashboard_visual"]
            )
        )
    if "generative_qn_a" in value:
        import aws_sdk_quicksight.types.registered_user_generative_qn_a_embedding_configuration

        out["GenerativeQnA"] = (
            aws_sdk_quicksight.types.registered_user_generative_qn_a_embedding_configuration.serialize_json(
                value["generative_qn_a"]
            )
        )
    if "quick_chat" in value:
        import aws_sdk_quicksight.types.registered_user_quick_chat_embedding_configuration

        out["QuickChat"] = (
            aws_sdk_quicksight.types.registered_user_quick_chat_embedding_configuration.serialize_json(
                value["quick_chat"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisteredUserEmbeddingExperienceConfiguration:
    out: RegisteredUserEmbeddingExperienceConfiguration = {}  # type: ignore[typeddict-item]
    if "Dashboard" in data:
        import aws_sdk_quicksight.types.registered_user_dashboard_embedding_configuration

        out["dashboard"] = (
            aws_sdk_quicksight.types.registered_user_dashboard_embedding_configuration.deserialize_json(
                data["Dashboard"]
            )
        )
    if "QuickSightConsole" in data:
        import aws_sdk_quicksight.types.registered_user_quick_sight_console_embedding_configuration

        out["quick_sight_console"] = (
            aws_sdk_quicksight.types.registered_user_quick_sight_console_embedding_configuration.deserialize_json(
                data["QuickSightConsole"]
            )
        )
    if "QSearchBar" in data:
        import aws_sdk_quicksight.types.registered_user_q_search_bar_embedding_configuration

        out["q_search_bar"] = (
            aws_sdk_quicksight.types.registered_user_q_search_bar_embedding_configuration.deserialize_json(
                data["QSearchBar"]
            )
        )
    if "DashboardVisual" in data:
        import aws_sdk_quicksight.types.registered_user_dashboard_visual_embedding_configuration

        out["dashboard_visual"] = (
            aws_sdk_quicksight.types.registered_user_dashboard_visual_embedding_configuration.deserialize_json(
                data["DashboardVisual"]
            )
        )
    if "GenerativeQnA" in data:
        import aws_sdk_quicksight.types.registered_user_generative_qn_a_embedding_configuration

        out["generative_qn_a"] = (
            aws_sdk_quicksight.types.registered_user_generative_qn_a_embedding_configuration.deserialize_json(
                data["GenerativeQnA"]
            )
        )
    if "QuickChat" in data:
        import aws_sdk_quicksight.types.registered_user_quick_chat_embedding_configuration

        out["quick_chat"] = (
            aws_sdk_quicksight.types.registered_user_quick_chat_embedding_configuration.deserialize_json(
                data["QuickChat"]
            )
        )
    return out
