"""Generated from Smithy shape ``com.amazonaws.glue#CustomAuthenticationProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.connector_property_list


class CustomAuthenticationProperties(TypedDict):
    authentication_parameters: (
        "aws_sdk_glue.types.connector_property_list.ConnectorPropertyList"
    )
    """<p>A map of custom authentication parameters that define the specific authentication mechanism and required properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomAuthenticationProperties) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.connector_property_list

    out["AuthenticationParameters"] = (
        aws_sdk_glue.types.connector_property_list.serialize_aws_json_1_1(
            value["authentication_parameters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomAuthenticationProperties:
    out: CustomAuthenticationProperties = {}  # type: ignore[typeddict-item]
    if "AuthenticationParameters" in data:
        import aws_sdk_glue.types.connector_property_list

        out["authentication_parameters"] = (
            aws_sdk_glue.types.connector_property_list.deserialize_aws_json_1_1(
                data["AuthenticationParameters"]
            )
        )
    else:
        raise DeserializationError(
            "CustomAuthenticationProperties.authentication_parameters required"
        )
    return out
