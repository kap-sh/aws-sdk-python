"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.application_ids_list


class DeleteApplicationsRequest(TypedDict):
    configuration_ids: "aws_sdk_application_discovery_service.types.application_ids_list.ApplicationIdsList"
    """<p>Configuration ID of an application to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationsRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.application_ids_list

    out["configurationIds"] = (
        aws_sdk_application_discovery_service.types.application_ids_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationsRequest:
    out: DeleteApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "configurationIds" in data:
        import aws_sdk_application_discovery_service.types.application_ids_list

        out["configuration_ids"] = (
            aws_sdk_application_discovery_service.types.application_ids_list.deserialize_aws_json_1_1(
                data["configurationIds"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteApplicationsRequest.configuration_ids required"
        )
    return out
