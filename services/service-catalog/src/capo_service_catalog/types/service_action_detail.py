"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.service_action_definition_map
    import capo_service_catalog.types.service_action_summary


class ServiceActionDetail(TypedDict, closed=True):
    service_action_summary: NotRequired[
        "capo_service_catalog.types.service_action_summary.ServiceActionSummary"
    ]
    """<p>Summary information about the self-service action.</p>"""
    definition: NotRequired[
        "capo_service_catalog.types.service_action_definition_map.ServiceActionDefinitionMap"
    ]
    """<p>A map that defines the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceActionDetail) -> dict:
    out: dict = {}
    if "service_action_summary" in value:
        import capo_service_catalog.types.service_action_summary

        out["ServiceActionSummary"] = (
            capo_service_catalog.types.service_action_summary.serialize_aws_json_1_1(
                value["service_action_summary"]
            )
        )
    if "definition" in value:
        import capo_service_catalog.types.service_action_definition_map

        out["Definition"] = (
            capo_service_catalog.types.service_action_definition_map.serialize_aws_json_1_1(
                value["definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceActionDetail:
    out: ServiceActionDetail = {}  # type: ignore[typeddict-item]
    if "ServiceActionSummary" in data:
        import capo_service_catalog.types.service_action_summary

        out["service_action_summary"] = (
            capo_service_catalog.types.service_action_summary.deserialize_aws_json_1_1(
                data["ServiceActionSummary"]
            )
        )
    if "Definition" in data:
        import capo_service_catalog.types.service_action_definition_map

        out["definition"] = (
            capo_service_catalog.types.service_action_definition_map.deserialize_aws_json_1_1(
                data["Definition"]
            )
        )
    return out
