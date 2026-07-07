"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceChangeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.causing_entity
    import aws_sdk_service_catalog.types.evaluation_type
    import aws_sdk_service_catalog.types.resource_target_definition


class ResourceChangeDetail(TypedDict, closed=True):
    target: NotRequired[
        "aws_sdk_service_catalog.types.resource_target_definition.ResourceTargetDefinition"
    ]
    """<p>Information about the resource attribute to be modified.</p>"""
    evaluation: NotRequired[
        "aws_sdk_service_catalog.types.evaluation_type.EvaluationType"
    ]
    """<p>For static evaluations, the value of the resource attribute will change and the new value is known. For dynamic evaluations, the value might change, and any new value will be determined when the plan is updated.</p>"""
    causing_entity: NotRequired[
        "aws_sdk_service_catalog.types.causing_entity.CausingEntity"
    ]
    """<p>The ID of the entity that caused the change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceChangeDetail) -> dict:
    out: dict = {}
    if "target" in value:
        import aws_sdk_service_catalog.types.resource_target_definition

        out["Target"] = (
            aws_sdk_service_catalog.types.resource_target_definition.serialize_aws_json_1_1(
                value["target"]
            )
        )
    if "evaluation" in value:
        import aws_sdk_service_catalog.types.evaluation_type

        out["Evaluation"] = (
            aws_sdk_service_catalog.types.evaluation_type.serialize_aws_json_1_1(
                value["evaluation"]
            )
        )
    if "causing_entity" in value:
        out["CausingEntity"] = value["causing_entity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceChangeDetail:
    out: ResourceChangeDetail = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        import aws_sdk_service_catalog.types.resource_target_definition

        out["target"] = (
            aws_sdk_service_catalog.types.resource_target_definition.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    if "Evaluation" in data:
        import aws_sdk_service_catalog.types.evaluation_type

        out["evaluation"] = (
            aws_sdk_service_catalog.types.evaluation_type.deserialize_aws_json_1_1(
                data["Evaluation"]
            )
        )
    if "CausingEntity" in data:
        out["causing_entity"] = data["CausingEntity"]
    return out
