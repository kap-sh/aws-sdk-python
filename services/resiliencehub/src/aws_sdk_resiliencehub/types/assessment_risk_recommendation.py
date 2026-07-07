"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AssessmentRiskRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_component_name_list
    import aws_sdk_resiliencehub.types.string255


class AssessmentRiskRecommendation(TypedDict, closed=True):
    risk: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Indicates the description of the potential risk identified in the application as part of the Resilience Hub assessment.</p> <note> <p>This property is available only in the US East (N. Virginia) Region.</p> </note>"""
    recommendation: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Indicates the recommendation provided by the Resilience Hub to address the identified risks in the application.</p> <note> <p>This property is available only in the US East (N. Virginia) Region.</p> </note>"""
    app_components: NotRequired[
        "aws_sdk_resiliencehub.types.app_component_name_list.AppComponentNameList"
    ]
    """<p>Indicates the Application Components (AppComponents) that were assessed as part of the assessment and are associated with the identified risk and recommendation.</p> <note> <p>This property is available only in the US East (N. Virginia) Region.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentRiskRecommendation) -> dict:
    out: dict = {}
    if "risk" in value:
        out["risk"] = value["risk"]
    if "recommendation" in value:
        out["recommendation"] = value["recommendation"]
    if "app_components" in value:
        import aws_sdk_resiliencehub.types.app_component_name_list

        out["appComponents"] = (
            aws_sdk_resiliencehub.types.app_component_name_list.serialize_json(
                value["app_components"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssessmentRiskRecommendation:
    out: AssessmentRiskRecommendation = {}  # type: ignore[typeddict-item]
    if "risk" in data:
        out["risk"] = data["risk"]
    if "recommendation" in data:
        out["recommendation"] = data["recommendation"]
    if "appComponents" in data:
        import aws_sdk_resiliencehub.types.app_component_name_list

        out["app_components"] = (
            aws_sdk_resiliencehub.types.app_component_name_list.deserialize_json(
                data["appComponents"]
            )
        )
    return out
