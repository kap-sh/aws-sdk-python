"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TestRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.alarm_reference_id_list
    import aws_sdk_resiliencehub.types.document_name
    import aws_sdk_resiliencehub.types.entity_description
    import aws_sdk_resiliencehub.types.entity_id
    import aws_sdk_resiliencehub.types.entity_name255
    import aws_sdk_resiliencehub.types.recommendation_item_list
    import aws_sdk_resiliencehub.types.recommendation_status
    import aws_sdk_resiliencehub.types.spec_reference_id
    import aws_sdk_resiliencehub.types.string500
    import aws_sdk_resiliencehub.types.test_risk
    import aws_sdk_resiliencehub.types.test_type
    import aws_sdk_resiliencehub.types.uuid


class TestRecommendation(TypedDict, closed=True):
    recommendation_id: NotRequired["aws_sdk_resiliencehub.types.uuid.Uuid"]
    """<p>Identifier for the test recommendation.</p>"""
    reference_id: "aws_sdk_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier for the test recommendation.</p>"""
    app_component_id: NotRequired[
        "aws_sdk_resiliencehub.types.entity_name255.EntityName255"
    ]
    """<p>Indicates the identifier of the AppComponent.</p>"""
    app_component_name: NotRequired["aws_sdk_resiliencehub.types.entity_id.EntityId"]
    """<p>Name of the Application Component.</p>"""
    name: NotRequired["aws_sdk_resiliencehub.types.document_name.DocumentName"]
    """<p>Name of the test recommendation.</p>"""
    intent: NotRequired[
        "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Intent of the test recommendation.</p>"""
    risk: NotRequired["aws_sdk_resiliencehub.types.test_risk.TestRisk"]
    """<p>Level of risk for this test recommendation.</p>"""
    type: NotRequired["aws_sdk_resiliencehub.types.test_type.TestType"]
    """<p>Type of test recommendation.</p>"""
    description: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Description for the test recommendation.</p>"""
    items: NotRequired[
        "aws_sdk_resiliencehub.types.recommendation_item_list.RecommendationItemList"
    ]
    """<p>The test recommendation items.</p>"""
    prerequisite: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Prerequisite of the test recommendation.</p>"""
    depends_on_alarms: NotRequired[
        "aws_sdk_resiliencehub.types.alarm_reference_id_list.AlarmReferenceIdList"
    ]
    """<p> A list of recommended alarms that are used in the test and must be exported before or with the test. </p>"""
    recommendation_status: NotRequired[
        "aws_sdk_resiliencehub.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Status of the recommended test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRecommendation) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    out["referenceId"] = value["reference_id"]
    if "app_component_id" in value:
        out["appComponentId"] = value["app_component_id"]
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "name" in value:
        out["name"] = value["name"]
    if "intent" in value:
        out["intent"] = value["intent"]
    if "risk" in value:
        import aws_sdk_resiliencehub.types.test_risk

        out["risk"] = aws_sdk_resiliencehub.types.test_risk.serialize_json(
            value["risk"]
        )
    if "type" in value:
        import aws_sdk_resiliencehub.types.test_type

        out["type"] = aws_sdk_resiliencehub.types.test_type.serialize_json(
            value["type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "items" in value:
        import aws_sdk_resiliencehub.types.recommendation_item_list

        out["items"] = (
            aws_sdk_resiliencehub.types.recommendation_item_list.serialize_json(
                value["items"]
            )
        )
    if "prerequisite" in value:
        out["prerequisite"] = value["prerequisite"]
    if "depends_on_alarms" in value:
        import aws_sdk_resiliencehub.types.alarm_reference_id_list

        out["dependsOnAlarms"] = (
            aws_sdk_resiliencehub.types.alarm_reference_id_list.serialize_json(
                value["depends_on_alarms"]
            )
        )
    if "recommendation_status" in value:
        import aws_sdk_resiliencehub.types.recommendation_status

        out["recommendationStatus"] = (
            aws_sdk_resiliencehub.types.recommendation_status.serialize_json(
                value["recommendation_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRecommendation:
    out: TestRecommendation = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    else:
        raise DeserializationError("TestRecommendation.reference_id required")
    if "appComponentId" in data:
        out["app_component_id"] = data["appComponentId"]
    if "appComponentName" in data:
        out["app_component_name"] = data["appComponentName"]
    if "name" in data:
        out["name"] = data["name"]
    if "intent" in data:
        out["intent"] = data["intent"]
    if "risk" in data:
        import aws_sdk_resiliencehub.types.test_risk

        out["risk"] = aws_sdk_resiliencehub.types.test_risk.deserialize_json(
            data["risk"]
        )
    if "type" in data:
        import aws_sdk_resiliencehub.types.test_type

        out["type"] = aws_sdk_resiliencehub.types.test_type.deserialize_json(
            data["type"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "items" in data:
        import aws_sdk_resiliencehub.types.recommendation_item_list

        out["items"] = (
            aws_sdk_resiliencehub.types.recommendation_item_list.deserialize_json(
                data["items"]
            )
        )
    if "prerequisite" in data:
        out["prerequisite"] = data["prerequisite"]
    if "dependsOnAlarms" in data:
        import aws_sdk_resiliencehub.types.alarm_reference_id_list

        out["depends_on_alarms"] = (
            aws_sdk_resiliencehub.types.alarm_reference_id_list.deserialize_json(
                data["dependsOnAlarms"]
            )
        )
    if "recommendationStatus" in data:
        import aws_sdk_resiliencehub.types.recommendation_status

        out["recommendation_status"] = (
            aws_sdk_resiliencehub.types.recommendation_status.deserialize_json(
                data["recommendationStatus"]
            )
        )
    return out
