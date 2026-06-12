"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_profile_detail_list
    import aws_sdk_appflow.types.next_token


class DescribeConnectorProfilesResponse(TypedDict):
    connector_profile_details: NotRequired[
        "aws_sdk_appflow.types.connector_profile_detail_list.ConnectorProfileDetailList"
    ]
    """<p> Returns information about the connector profiles associated with the flow. </p>"""
    next_token: NotRequired["aws_sdk_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. If <code>nextToken=null</code>, this means that all records have been fetched. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorProfilesResponse) -> dict:
    out: dict = {}
    if "connector_profile_details" in value:
        import aws_sdk_appflow.types.connector_profile_detail_list

        out["connectorProfileDetails"] = (
            aws_sdk_appflow.types.connector_profile_detail_list.serialize_json(
                value["connector_profile_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorProfilesResponse:
    out: DescribeConnectorProfilesResponse = {}  # type: ignore[typeddict-item]
    if "connectorProfileDetails" in data:
        import aws_sdk_appflow.types.connector_profile_detail_list

        out["connector_profile_details"] = (
            aws_sdk_appflow.types.connector_profile_detail_list.deserialize_json(
                data["connectorProfileDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
