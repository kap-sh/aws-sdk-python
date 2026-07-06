"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateNotebookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.cell_order
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_config
    import aws_sdk_datazone.types.metadata
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.notebook_name
    import aws_sdk_datazone.types.notebook_status
    import aws_sdk_datazone.types.parameters


class UpdateNotebookInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>"""
    identifier: "aws_sdk_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook to update.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The updated description of the notebook.</p>"""
    status: NotRequired["aws_sdk_datazone.types.notebook_status.NotebookStatus"]
    """<p>The updated status of the notebook.</p>"""
    name: NotRequired["aws_sdk_datazone.types.notebook_name.NotebookName"]
    """<p>The updated name of the notebook.</p>"""
    cell_order: NotRequired["aws_sdk_datazone.types.cell_order.CellOrder"]
    """<p>The updated ordered list of cells in the notebook.</p>"""
    metadata: NotRequired["aws_sdk_datazone.types.metadata.Metadata"]
    """<p>The updated metadata for the notebook, specified as key-value pairs.</p>"""
    parameters: NotRequired["aws_sdk_datazone.types.parameters.Parameters"]
    """<p>The updated sensitive parameters for the notebook, specified as key-value pairs.</p>"""
    environment_configuration: NotRequired[
        "aws_sdk_datazone.types.environment_config.EnvironmentConfig"
    ]
    """<p>The updated environment configuration for the notebook.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotebookInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_datazone.types.notebook_status

        out["status"] = aws_sdk_datazone.types.notebook_status.serialize_json(
            value["status"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "cell_order" in value:
        import aws_sdk_datazone.types.cell_order

        out["cellOrder"] = aws_sdk_datazone.types.cell_order.serialize_json(
            value["cell_order"]
        )
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
    if "environment_configuration" in value:
        import aws_sdk_datazone.types.environment_config

        out["environmentConfiguration"] = (
            aws_sdk_datazone.types.environment_config.serialize_json(
                value["environment_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateNotebookInput:
    out: UpdateNotebookInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_datazone.types.notebook_status

        out["status"] = aws_sdk_datazone.types.notebook_status.deserialize_json(
            data["status"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "cellOrder" in data:
        import aws_sdk_datazone.types.cell_order

        out["cell_order"] = aws_sdk_datazone.types.cell_order.deserialize_json(
            data["cellOrder"]
        )
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
    if "environmentConfiguration" in data:
        import aws_sdk_datazone.types.environment_config

        out["environment_configuration"] = (
            aws_sdk_datazone.types.environment_config.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
