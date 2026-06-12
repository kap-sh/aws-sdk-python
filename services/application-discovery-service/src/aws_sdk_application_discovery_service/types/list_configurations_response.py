"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ListConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configurations
    import aws_sdk_application_discovery_service.types.next_token


class ListConfigurationsResponse(TypedDict):
    configurations: NotRequired[
        "aws_sdk_application_discovery_service.types.configurations.Configurations"
    ]
    """<p>Returns configuration details, including the configuration ID, attribute names, and attribute values.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>Token to retrieve the next set of results. For example, if your call to ListConfigurations returned 100 items, but you set <code>ListConfigurationsRequest$maxResults</code> to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConfigurationsResponse) -> dict:
    out: dict = {}
    if "configurations" in value:
        import aws_sdk_application_discovery_service.types.configurations

        out["configurations"] = (
            aws_sdk_application_discovery_service.types.configurations.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConfigurationsResponse:
    out: ListConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "configurations" in data:
        import aws_sdk_application_discovery_service.types.configurations

        out["configurations"] = (
            aws_sdk_application_discovery_service.types.configurations.deserialize_aws_json_1_1(
                data["configurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
