"""Generated from Smithy shape ``com.amazonaws.datazone#CreateNotebookInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.metadata
    import aws_sdk_datazone.types.notebook_name
    import aws_sdk_datazone.types.parameters
    import aws_sdk_datazone.types.project_id


class CreateNotebookInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to create the notebook.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    name: "aws_sdk_datazone.types.notebook_name.NotebookName"
    """<p>The name of the notebook. The name must be between 1 and 256 characters.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the notebook.</p>"""
    metadata: NotRequired["aws_sdk_datazone.types.metadata.Metadata"]
    """<p>The metadata for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>"""
    parameters: NotRequired["aws_sdk_datazone.types.parameters.Parameters"]
    """<p>The sensitive parameters for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotebookInput) -> dict:
    out: dict = {}
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "metadata" in value:
        import aws_sdk_datazone.types.metadata

        out["metadata"] = aws_sdk_datazone.types.metadata.serialize_json(
            value["metadata"]
        )
    if "parameters" in value:
        import aws_sdk_datazone.types.parameters

        out["parameters"] = aws_sdk_datazone.types.parameters.serialize_json(
            value["parameters"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateNotebookInput:
    out: CreateNotebookInput = {}  # type: ignore[typeddict-item]
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateNotebookInput.owning_project_identifier required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateNotebookInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "metadata" in data:
        import aws_sdk_datazone.types.metadata

        out["metadata"] = aws_sdk_datazone.types.metadata.deserialize_json(
            data["metadata"]
        )
    if "parameters" in data:
        import aws_sdk_datazone.types.parameters

        out["parameters"] = aws_sdk_datazone.types.parameters.deserialize_json(
            data["parameters"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
