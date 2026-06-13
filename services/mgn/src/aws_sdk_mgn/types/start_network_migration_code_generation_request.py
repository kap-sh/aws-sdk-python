"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationCodeGenerationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.code_generation_output_format_types
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id


class StartNetworkMigrationCodeGenerationRequest(TypedDict):
    network_migration_execution_id: (
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    code_generation_output_format_types: NotRequired[
        "aws_sdk_mgn.types.code_generation_output_format_types.CodeGenerationOutputFormatTypes"
    ]
    """<p>The output format types for code generation, such as CloudFormation or Terraform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationCodeGenerationRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "code_generation_output_format_types" in value:
        import aws_sdk_mgn.types.code_generation_output_format_types

        out["codeGenerationOutputFormatTypes"] = (
            aws_sdk_mgn.types.code_generation_output_format_types.serialize_json(
                value["code_generation_output_format_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationCodeGenerationRequest:
    out: StartNetworkMigrationCodeGenerationRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationCodeGenerationRequest.network_migration_execution_id required"
        )
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationCodeGenerationRequest.network_migration_definition_id required"
        )
    if "codeGenerationOutputFormatTypes" in data:
        import aws_sdk_mgn.types.code_generation_output_format_types

        out["code_generation_output_format_types"] = (
            aws_sdk_mgn.types.code_generation_output_format_types.deserialize_json(
                data["codeGenerationOutputFormatTypes"]
            )
        )
    return out
