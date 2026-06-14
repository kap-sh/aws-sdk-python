"""Generated from Smithy shape ``com.amazonaws.datazone#CreateConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_location
    import aws_sdk_datazone.types.configurations
    import aws_sdk_datazone.types.connection_name
    import aws_sdk_datazone.types.connection_properties_input
    import aws_sdk_datazone.types.connection_scope
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id


class CreateConnectionInput(TypedDict):
    aws_location: NotRequired["aws_sdk_datazone.types.aws_location.AwsLocation"]
    """<p>The location where the connection is created.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    configurations: NotRequired["aws_sdk_datazone.types.configurations.Configurations"]
    """<p>The configurations of the connection.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>A connection description.</p>"""
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the connection is created.</p>"""
    environment_identifier: NotRequired[
        "aws_sdk_datazone.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment where the connection is created.</p>"""
    name: "aws_sdk_datazone.types.connection_name.ConnectionName"
    """<p>The connection name.</p>"""
    props: NotRequired[
        "aws_sdk_datazone.types.connection_properties_input.ConnectionPropertiesInput"
    ]
    """<p>The connection props.</p>"""
    enable_trusted_identity_propagation: NotRequired["bool"]
    """<p>Specifies whether the trusted identity propagation is enabled.</p>"""
    scope: NotRequired["aws_sdk_datazone.types.connection_scope.ConnectionScope"]
    """<p>The scope of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectionInput) -> dict:
    out: dict = {}
    if "aws_location" in value:
        import aws_sdk_datazone.types.aws_location

        out["awsLocation"] = aws_sdk_datazone.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "configurations" in value:
        import aws_sdk_datazone.types.configurations

        out["configurations"] = aws_sdk_datazone.types.configurations.serialize_json(
            value["configurations"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "environment_identifier" in value:
        out["environmentIdentifier"] = value["environment_identifier"]
    out["name"] = value["name"]
    if "props" in value:
        import aws_sdk_datazone.types.connection_properties_input

        out["props"] = (
            aws_sdk_datazone.types.connection_properties_input.serialize_json(
                value["props"]
            )
        )
    if "enable_trusted_identity_propagation" in value:
        out["enableTrustedIdentityPropagation"] = value[
            "enable_trusted_identity_propagation"
        ]
    if "scope" in value:
        import aws_sdk_datazone.types.connection_scope

        out["scope"] = aws_sdk_datazone.types.connection_scope.serialize_json(
            value["scope"]
        )
    return out


def deserialize_json(data: dict) -> CreateConnectionInput:
    out: CreateConnectionInput = {}  # type: ignore[typeddict-item]
    if "awsLocation" in data:
        import aws_sdk_datazone.types.aws_location

        out["aws_location"] = aws_sdk_datazone.types.aws_location.deserialize_json(
            data["awsLocation"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "configurations" in data:
        import aws_sdk_datazone.types.configurations

        out["configurations"] = aws_sdk_datazone.types.configurations.deserialize_json(
            data["configurations"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "environmentIdentifier" in data:
        out["environment_identifier"] = data["environmentIdentifier"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateConnectionInput.name required")
    if "props" in data:
        import aws_sdk_datazone.types.connection_properties_input

        out["props"] = (
            aws_sdk_datazone.types.connection_properties_input.deserialize_json(
                data["props"]
            )
        )
    if "enableTrustedIdentityPropagation" in data:
        out["enable_trusted_identity_propagation"] = data[
            "enableTrustedIdentityPropagation"
        ]
    if "scope" in data:
        import aws_sdk_datazone.types.connection_scope

        out["scope"] = aws_sdk_datazone.types.connection_scope.deserialize_json(
            data["scope"]
        )
    return out
