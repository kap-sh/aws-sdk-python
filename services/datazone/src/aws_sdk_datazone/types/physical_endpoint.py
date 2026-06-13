"""Generated from Smithy shape ``com.amazonaws.datazone#PhysicalEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_location
    import aws_sdk_datazone.types.glue_connection
    import aws_sdk_datazone.types.glue_connection_names
    import aws_sdk_datazone.types.protocol


class PhysicalEndpoint(TypedDict):
    aws_location: NotRequired["aws_sdk_datazone.types.aws_location.AwsLocation"]
    """<p>The location of a connection.</p>"""
    glue_connection_name: NotRequired["str"]
    """<p>The Amazon Web Services Glue connection name.</p>"""
    glue_connection_names: NotRequired[
        "aws_sdk_datazone.types.glue_connection_names.GlueConnectionNames"
    ]
    """<p>The Amazon Web Services Glue connection names in the physical endpoint.</p>"""
    glue_connection: NotRequired[
        "aws_sdk_datazone.types.glue_connection.GlueConnection"
    ]
    """<p>The Amazon Web Services Glue connection.</p>"""
    enable_trusted_identity_propagation: NotRequired["bool"]
    """<p>Specified whether trusted identity propagation for the connection is enabled.</p>"""
    host: NotRequired["str"]
    """<p>The host in the physical endpoints of a connection.</p>"""
    port: NotRequired["int"]
    """<p>The port in the physical endpoints of a connection.</p>"""
    protocol: NotRequired["aws_sdk_datazone.types.protocol.Protocol"]
    """<p>The protocol in the physical endpoints of a connection.</p>"""
    stage: NotRequired["str"]
    """<p>The stage in the physical endpoints of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalEndpoint) -> dict:
    out: dict = {}
    if "aws_location" in value:
        import aws_sdk_datazone.types.aws_location

        out["awsLocation"] = aws_sdk_datazone.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "glue_connection_name" in value:
        out["glueConnectionName"] = value["glue_connection_name"]
    if "glue_connection_names" in value:
        import aws_sdk_datazone.types.glue_connection_names

        out["glueConnectionNames"] = (
            aws_sdk_datazone.types.glue_connection_names.serialize_json(
                value["glue_connection_names"]
            )
        )
    if "glue_connection" in value:
        import aws_sdk_datazone.types.glue_connection

        out["glueConnection"] = aws_sdk_datazone.types.glue_connection.serialize_json(
            value["glue_connection"]
        )
    if "enable_trusted_identity_propagation" in value:
        out["enableTrustedIdentityPropagation"] = value[
            "enable_trusted_identity_propagation"
        ]
    if "host" in value:
        out["host"] = value["host"]
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        import aws_sdk_datazone.types.protocol

        out["protocol"] = aws_sdk_datazone.types.protocol.serialize_json(
            value["protocol"]
        )
    if "stage" in value:
        out["stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> PhysicalEndpoint:
    out: PhysicalEndpoint = {}  # type: ignore[typeddict-item]
    if "awsLocation" in data:
        import aws_sdk_datazone.types.aws_location

        out["aws_location"] = aws_sdk_datazone.types.aws_location.deserialize_json(
            data["awsLocation"]
        )
    if "glueConnectionName" in data:
        out["glue_connection_name"] = data["glueConnectionName"]
    if "glueConnectionNames" in data:
        import aws_sdk_datazone.types.glue_connection_names

        out["glue_connection_names"] = (
            aws_sdk_datazone.types.glue_connection_names.deserialize_json(
                data["glueConnectionNames"]
            )
        )
    if "glueConnection" in data:
        import aws_sdk_datazone.types.glue_connection

        out["glue_connection"] = (
            aws_sdk_datazone.types.glue_connection.deserialize_json(
                data["glueConnection"]
            )
        )
    if "enableTrustedIdentityPropagation" in data:
        out["enable_trusted_identity_propagation"] = data[
            "enableTrustedIdentityPropagation"
        ]
    if "host" in data:
        out["host"] = data["host"]
    if "port" in data:
        out["port"] = data["port"]
    if "protocol" in data:
        import aws_sdk_datazone.types.protocol

        out["protocol"] = aws_sdk_datazone.types.protocol.deserialize_json(
            data["protocol"]
        )
    if "stage" in data:
        out["stage"] = data["stage"]
    return out
