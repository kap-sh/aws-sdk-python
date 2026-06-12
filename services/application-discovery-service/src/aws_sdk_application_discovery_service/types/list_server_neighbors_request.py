"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ListServerNeighborsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.boolean
    import aws_sdk_application_discovery_service.types.configuration_id
    import aws_sdk_application_discovery_service.types.configuration_id_list
    import aws_sdk_application_discovery_service.types.integer
    import aws_sdk_application_discovery_service.types.string


class ListServerNeighborsRequest(TypedDict):
    configuration_id: (
        "aws_sdk_application_discovery_service.types.configuration_id.ConfigurationId"
    )
    """<p>Configuration ID of the server for which neighbors are being listed.</p>"""
    port_information_needed: (
        "aws_sdk_application_discovery_service.types.boolean.Boolean"
    )
    """<p>Flag to indicate if port and protocol information is needed as part of the response.</p>"""
    neighbor_configuration_ids: NotRequired[
        "aws_sdk_application_discovery_service.types.configuration_id_list.ConfigurationIdList"
    ]
    """<p>List of configuration IDs to test for one-hop-away.</p>"""
    max_results: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>Maximum number of results to return in a single page of output.</p>"""
    next_token: NotRequired["aws_sdk_application_discovery_service.types.string.String"]
    """<p>Token to retrieve the next set of results. For example, if you previously specified 100 IDs for <code>ListServerNeighborsRequest$neighborConfigurationIds</code> but set <code>ListServerNeighborsRequest$maxResults</code> to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServerNeighborsRequest) -> dict:
    out: dict = {}
    out["configurationId"] = value["configuration_id"]
    out["portInformationNeeded"] = value.get("port_information_needed", False)
    if "neighbor_configuration_ids" in value:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["neighborConfigurationIds"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.serialize_aws_json_1_1(
                value["neighbor_configuration_ids"]
            )
        )
    out["maxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServerNeighborsRequest:
    out: ListServerNeighborsRequest = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    else:
        raise DeserializationError(
            "ListServerNeighborsRequest.configuration_id required"
        )
    if "portInformationNeeded" in data:
        out["port_information_needed"] = data["portInformationNeeded"]
    else:
        out["port_information_needed"] = False
    if "neighborConfigurationIds" in data:
        import aws_sdk_application_discovery_service.types.configuration_id_list

        out["neighbor_configuration_ids"] = (
            aws_sdk_application_discovery_service.types.configuration_id_list.deserialize_aws_json_1_1(
                data["neighborConfigurationIds"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
