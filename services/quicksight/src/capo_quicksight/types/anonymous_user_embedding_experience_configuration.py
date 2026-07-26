"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserEmbeddingExperienceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration
    import capo_quicksight.types.anonymous_user_dashboard_visual_embedding_configuration
    import capo_quicksight.types.anonymous_user_generative_qn_a_embedding_configuration
    import capo_quicksight.types.anonymous_user_q_search_bar_embedding_configuration


class AnonymousUserEmbeddingExperienceConfiguration(TypedDict, closed=True):
    dashboard: NotRequired[
        "capo_quicksight.types.anonymous_user_dashboard_embedding_configuration.AnonymousUserDashboardEmbeddingConfiguration"
    ]
    """<p>The type of embedding experience. In this case, Amazon Quick Sight dashboards.</p>"""
    dashboard_visual: NotRequired[
        "capo_quicksight.types.anonymous_user_dashboard_visual_embedding_configuration.AnonymousUserDashboardVisualEmbeddingConfiguration"
    ]
    """<p>The type of embedding experience. In this case, Amazon Quick Sight visuals.</p>"""
    q_search_bar: NotRequired[
        "capo_quicksight.types.anonymous_user_q_search_bar_embedding_configuration.AnonymousUserQSearchBarEmbeddingConfiguration"
    ]
    """<p>The Q search bar that you want to use for anonymous user embedding.</p>"""
    generative_qn_a: NotRequired[
        "capo_quicksight.types.anonymous_user_generative_qn_a_embedding_configuration.AnonymousUserGenerativeQnAEmbeddingConfiguration"
    ]
    """<p>The Generative Q&A experience that you want to use for anonymous user embedding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnonymousUserEmbeddingExperienceConfiguration) -> dict:
    out: dict = {}
    if "dashboard" in value:
        import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration

        out["Dashboard"] = (
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration.serialize_json(
                value["dashboard"]
            )
        )
    if "dashboard_visual" in value:
        import capo_quicksight.types.anonymous_user_dashboard_visual_embedding_configuration

        out["DashboardVisual"] = (
            capo_quicksight.types.anonymous_user_dashboard_visual_embedding_configuration.serialize_json(
                value["dashboard_visual"]
            )
        )
    if "q_search_bar" in value:
        import capo_quicksight.types.anonymous_user_q_search_bar_embedding_configuration

        out["QSearchBar"] = (
            capo_quicksight.types.anonymous_user_q_search_bar_embedding_configuration.serialize_json(
                value["q_search_bar"]
            )
        )
    if "generative_qn_a" in value:
        import capo_quicksight.types.anonymous_user_generative_qn_a_embedding_configuration

        out["GenerativeQnA"] = (
            capo_quicksight.types.anonymous_user_generative_qn_a_embedding_configuration.serialize_json(
                value["generative_qn_a"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnonymousUserEmbeddingExperienceConfiguration:
    out: AnonymousUserEmbeddingExperienceConfiguration = {}  # type: ignore[typeddict-item]
    if "Dashboard" in data:
        import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration

        out["dashboard"] = (
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration.deserialize_json(
                data["Dashboard"]
            )
        )
    if "DashboardVisual" in data:
        import capo_quicksight.types.anonymous_user_dashboard_visual_embedding_configuration

        out["dashboard_visual"] = (
            capo_quicksight.types.anonymous_user_dashboard_visual_embedding_configuration.deserialize_json(
                data["DashboardVisual"]
            )
        )
    if "QSearchBar" in data:
        import capo_quicksight.types.anonymous_user_q_search_bar_embedding_configuration

        out["q_search_bar"] = (
            capo_quicksight.types.anonymous_user_q_search_bar_embedding_configuration.deserialize_json(
                data["QSearchBar"]
            )
        )
    if "GenerativeQnA" in data:
        import capo_quicksight.types.anonymous_user_generative_qn_a_embedding_configuration

        out["generative_qn_a"] = (
            capo_quicksight.types.anonymous_user_generative_qn_a_embedding_configuration.deserialize_json(
                data["GenerativeQnA"]
            )
        )
    return out
