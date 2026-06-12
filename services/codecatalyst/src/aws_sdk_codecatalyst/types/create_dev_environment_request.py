"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateDevEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.client_token
    import aws_sdk_codecatalyst.types.ide_configuration_list
    import aws_sdk_codecatalyst.types.inactivity_timeout_minutes
    import aws_sdk_codecatalyst.types.instance_type
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.persistent_storage_configuration
    import aws_sdk_codecatalyst.types.repositories_input


class CreateDevEnvironmentRequest(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    repositories: NotRequired[
        "aws_sdk_codecatalyst.types.repositories_input.RepositoriesInput"
    ]
    """<p>The source repository that contains the branch to clone into the Dev Environment. </p>"""
    client_token: NotRequired["aws_sdk_codecatalyst.types.client_token.ClientToken"]
    """<p>A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.</p>"""
    alias: NotRequired["str"]
    """<p>The user-defined alias for a Dev Environment.</p>"""
    ides: NotRequired[
        "aws_sdk_codecatalyst.types.ide_configuration_list.IdeConfigurationList"
    ]
    """<p>Information about the integrated development environment (IDE) configured for a Dev Environment.</p> <note> <p>An IDE is required to create a Dev Environment. For Dev Environment creation, this field contains configuration information and must be provided. </p> </note>"""
    instance_type: "aws_sdk_codecatalyst.types.instance_type.InstanceType"
    """<p>The Amazon EC2 instace type to use for the Dev Environment. </p>"""
    inactivity_timeout_minutes: (
        "aws_sdk_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
    )
    """<p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.</p>"""
    persistent_storage: "aws_sdk_codecatalyst.types.persistent_storage_configuration.PersistentStorageConfiguration"
    """<p>Information about the amount of storage allocated to the Dev Environment. </p> <note> <p>By default, a Dev Environment is configured to have 16GB of persistent storage when created from the Amazon CodeCatalyst console, but there is no default when programmatically creating a Dev Environment. Valid values for persistent storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.</p> </note>"""
    vpc_connection_name: NotRequired[
        "aws_sdk_codecatalyst.types.name_string.NameString"
    ]
    """<p>The name of the connection that will be used to connect to Amazon VPC, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDevEnvironmentRequest) -> dict:
    out: dict = {}
    if "repositories" in value:
        import aws_sdk_codecatalyst.types.repositories_input

        out["repositories"] = (
            aws_sdk_codecatalyst.types.repositories_input.serialize_json(
                value["repositories"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "ides" in value:
        import aws_sdk_codecatalyst.types.ide_configuration_list

        out["ides"] = aws_sdk_codecatalyst.types.ide_configuration_list.serialize_json(
            value["ides"]
        )
    out["instanceType"] = value["instance_type"]
    out["inactivityTimeoutMinutes"] = value.get("inactivity_timeout_minutes", 0)
    import aws_sdk_codecatalyst.types.persistent_storage_configuration

    out["persistentStorage"] = (
        aws_sdk_codecatalyst.types.persistent_storage_configuration.serialize_json(
            value["persistent_storage"]
        )
    )
    if "vpc_connection_name" in value:
        out["vpcConnectionName"] = value["vpc_connection_name"]
    return out


def deserialize_json(data: dict) -> CreateDevEnvironmentRequest:
    out: CreateDevEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import aws_sdk_codecatalyst.types.repositories_input

        out["repositories"] = (
            aws_sdk_codecatalyst.types.repositories_input.deserialize_json(
                data["repositories"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "alias" in data:
        out["alias"] = data["alias"]
    if "ides" in data:
        import aws_sdk_codecatalyst.types.ide_configuration_list

        out["ides"] = (
            aws_sdk_codecatalyst.types.ide_configuration_list.deserialize_json(
                data["ides"]
            )
        )
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("CreateDevEnvironmentRequest.instance_type required")
    if "inactivityTimeoutMinutes" in data:
        out["inactivity_timeout_minutes"] = data["inactivityTimeoutMinutes"]
    else:
        out["inactivity_timeout_minutes"] = 0
    if "persistentStorage" in data:
        import aws_sdk_codecatalyst.types.persistent_storage_configuration

        out["persistent_storage"] = (
            aws_sdk_codecatalyst.types.persistent_storage_configuration.deserialize_json(
                data["persistentStorage"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDevEnvironmentRequest.persistent_storage required"
        )
    if "vpcConnectionName" in data:
        out["vpc_connection_name"] = data["vpcConnectionName"]
    return out
