"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DisassociateConfigurationItemsFromApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.application_id
    import aws_sdk_application_discovery_service.types.configuration_id_list


class DisassociateConfigurationItemsFromApplicationRequest(TypedDict, closed=True):
    application_configuration_id: (
        "aws_sdk_application_discovery_service.types.application_id.ApplicationId"
    )
    """<p>Configuration ID of an application from which each item is disassociated.</p>"""
    configuration_ids: "aws_sdk_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    """<p>Configuration ID of each item to be disassociated from an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateConfigurationItemsFromApplicationRequest,
) -> dict:
    out: dict = {}
    out["applicationConfigurationId"] = value["application_configuration_id"]
    import aws_sdk_application_discovery_service.types.configuration_id_list

    out["configurationIds"] = (
        aws_sdk_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateConfigurationItemsFromApplicationRequest:
    out: DisassociateConfigurationItemsFromApplicationRequest = {}  # type: ignore[typeddict-item]
    if "applicationConfigurationId" in data:
        out["application_configuration_id"] = data["applicationConfigurationId"]
    else:
        raise DeserializationError(
            "DisassociateConfigurationItemsFromApplicationRequest.application_configuration_id required"
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
            "DisassociateConfigurationItemsFromApplicationRequest.configuration_ids required"
        )
    return out
