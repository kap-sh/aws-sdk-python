"""Generated from Smithy shape ``com.amazonaws.glue#ListIntegrationResourcePropertiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_resource_property_list
    import capo_glue.types.string1024


class ListIntegrationResourcePropertiesResponse(TypedDict, closed=True):
    integration_resource_property_list: NotRequired[
        "capo_glue.types.integration_resource_property_list.IntegrationResourcePropertyList"
    ]
    """<p>A list of integration resource property meeting the filter criteria.</p>"""
    marker: NotRequired["capo_glue.types.string1024.String1024"]
    """<p>This is the pagination token for the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIntegrationResourcePropertiesResponse) -> dict:
    out: dict = {}
    if "integration_resource_property_list" in value:
        import capo_glue.types.integration_resource_property_list

        out["IntegrationResourcePropertyList"] = (
            capo_glue.types.integration_resource_property_list.serialize_aws_json_1_1(
                value["integration_resource_property_list"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIntegrationResourcePropertiesResponse:
    out: ListIntegrationResourcePropertiesResponse = {}  # type: ignore[typeddict-item]
    if "IntegrationResourcePropertyList" in data:
        import capo_glue.types.integration_resource_property_list

        out["integration_resource_property_list"] = (
            capo_glue.types.integration_resource_property_list.deserialize_aws_json_1_1(
                data["IntegrationResourcePropertyList"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
