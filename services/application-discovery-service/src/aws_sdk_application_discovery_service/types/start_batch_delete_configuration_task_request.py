"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartBatchDeleteConfigurationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration_id_list
    import aws_sdk_application_discovery_service.types.deletion_configuration_item_type


class StartBatchDeleteConfigurationTaskRequest(TypedDict, closed=True):
    configuration_type: "aws_sdk_application_discovery_service.types.deletion_configuration_item_type.DeletionConfigurationItemType"
    """<p> The type of configuration item to delete. Supported types are: SERVER. </p>"""
    configuration_ids: "aws_sdk_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    """<p> The list of configuration IDs that will be deleted by the task. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBatchDeleteConfigurationTaskRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.deletion_configuration_item_type

    out["configurationType"] = (
        aws_sdk_application_discovery_service.types.deletion_configuration_item_type.serialize_aws_json_1_1(
            value["configuration_type"]
        )
    )
    import aws_sdk_application_discovery_service.types.configuration_id_list

    out["configurationIds"] = (
        aws_sdk_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBatchDeleteConfigurationTaskRequest:
    out: StartBatchDeleteConfigurationTaskRequest = {}  # type: ignore[typeddict-item]
    if "configurationType" in data:
        import aws_sdk_application_discovery_service.types.deletion_configuration_item_type

        out["configuration_type"] = (
            aws_sdk_application_discovery_service.types.deletion_configuration_item_type.deserialize_aws_json_1_1(
                data["configurationType"]
            )
        )
    else:
        raise DeserializationError(
            "StartBatchDeleteConfigurationTaskRequest.configuration_type required"
        )
    if "configurationIds" in data:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["configuration_ids"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["configurationIds"]
            )
        )
    else:
        raise DeserializationError(
            "StartBatchDeleteConfigurationTaskRequest.configuration_ids required"
        )
    return out
