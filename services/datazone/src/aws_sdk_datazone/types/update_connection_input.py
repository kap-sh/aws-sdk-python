"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_location
    import aws_sdk_datazone.types.configurations
    import aws_sdk_datazone.types.connection_id
    import aws_sdk_datazone.types.connection_properties_patch
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id


class UpdateConnectionInput(TypedDict, closed=True):
    configurations: NotRequired["aws_sdk_datazone.types.configurations.Configurations"]
    """<p>The configurations of the connection.</p>"""
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where a connection is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.connection_id.ConnectionId"
    """<p>The ID of the connection to be updated.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of a connection.</p>"""
    aws_location: NotRequired["aws_sdk_datazone.types.aws_location.AwsLocation"]
    """<p>The location where a connection is to be updated.</p>"""
    props: NotRequired[
        "aws_sdk_datazone.types.connection_properties_patch.ConnectionPropertiesPatch"
    ]
    """<p>The connection props.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectionInput) -> dict:
    out: dict = {}
    if "configurations" in value:
        import aws_sdk_datazone.types.configurations

        out["configurations"] = aws_sdk_datazone.types.configurations.serialize_json(
            value["configurations"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "aws_location" in value:
        import aws_sdk_datazone.types.aws_location

        out["awsLocation"] = aws_sdk_datazone.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "props" in value:
        import aws_sdk_datazone.types.connection_properties_patch

        out["props"] = (
            aws_sdk_datazone.types.connection_properties_patch.serialize_json(
                value["props"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectionInput:
    out: UpdateConnectionInput = {}  # type: ignore[typeddict-item]
    if "configurations" in data:
        import aws_sdk_datazone.types.configurations

        out["configurations"] = aws_sdk_datazone.types.configurations.deserialize_json(
            data["configurations"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "awsLocation" in data:
        import aws_sdk_datazone.types.aws_location

        out["aws_location"] = aws_sdk_datazone.types.aws_location.deserialize_json(
            data["awsLocation"]
        )
    if "props" in data:
        import aws_sdk_datazone.types.connection_properties_patch

        out["props"] = (
            aws_sdk_datazone.types.connection_properties_patch.deserialize_json(
                data["props"]
            )
        )
    return out
