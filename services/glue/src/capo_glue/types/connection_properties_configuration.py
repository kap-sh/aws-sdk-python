"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionPropertiesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connector_property
    import capo_glue.types.connector_property_list


class ConnectionPropertiesConfiguration(TypedDict, closed=True):
    url: NotRequired["capo_glue.types.connector_property.ConnectorProperty"]
    """<p>The base instance URL for the endpoint that this connection type will connect to.</p>"""
    additional_request_parameters: NotRequired[
        "capo_glue.types.connector_property_list.ConnectorPropertyList"
    ]
    """<p>Key-value pairs of additional request parameters that may be needed during connection creation, such as API versions or service-specific configuration options.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionPropertiesConfiguration) -> dict:
    out: dict = {}
    if "url" in value:
        import capo_glue.types.connector_property

        out["Url"] = capo_glue.types.connector_property.serialize_aws_json_1_1(
            value["url"]
        )
    if "additional_request_parameters" in value:
        import capo_glue.types.connector_property_list

        out["AdditionalRequestParameters"] = (
            capo_glue.types.connector_property_list.serialize_aws_json_1_1(
                value["additional_request_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionPropertiesConfiguration:
    out: ConnectionPropertiesConfiguration = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        import capo_glue.types.connector_property

        out["url"] = capo_glue.types.connector_property.deserialize_aws_json_1_1(
            data["Url"]
        )
    if "AdditionalRequestParameters" in data:
        import capo_glue.types.connector_property_list

        out["additional_request_parameters"] = (
            capo_glue.types.connector_property_list.deserialize_aws_json_1_1(
                data["AdditionalRequestParameters"]
            )
        )
    return out
