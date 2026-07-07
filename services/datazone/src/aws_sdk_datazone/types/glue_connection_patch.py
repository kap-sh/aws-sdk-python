"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnectionPatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.authentication_configuration_patch
    import aws_sdk_datazone.types.connection_properties


class GlueConnectionPatch(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>The description of the Amazon Web Services Glue connection patch.</p>"""
    connection_properties: NotRequired[
        "aws_sdk_datazone.types.connection_properties.ConnectionProperties"
    ]
    """<p>The properties of the Amazon Web Services Glue connection patch.</p>"""
    authentication_configuration: NotRequired[
        "aws_sdk_datazone.types.authentication_configuration_patch.AuthenticationConfigurationPatch"
    ]
    """<p>The authentication configuration of the Amazon Web Services Glue connection patch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueConnectionPatch) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "connection_properties" in value:
        import aws_sdk_datazone.types.connection_properties

        out["connectionProperties"] = (
            aws_sdk_datazone.types.connection_properties.serialize_json(
                value["connection_properties"]
            )
        )
    if "authentication_configuration" in value:
        import aws_sdk_datazone.types.authentication_configuration_patch

        out["authenticationConfiguration"] = (
            aws_sdk_datazone.types.authentication_configuration_patch.serialize_json(
                value["authentication_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlueConnectionPatch:
    out: GlueConnectionPatch = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "connectionProperties" in data:
        import aws_sdk_datazone.types.connection_properties

        out["connection_properties"] = (
            aws_sdk_datazone.types.connection_properties.deserialize_json(
                data["connectionProperties"]
            )
        )
    if "authenticationConfiguration" in data:
        import aws_sdk_datazone.types.authentication_configuration_patch

        out["authentication_configuration"] = (
            aws_sdk_datazone.types.authentication_configuration_patch.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    return out
