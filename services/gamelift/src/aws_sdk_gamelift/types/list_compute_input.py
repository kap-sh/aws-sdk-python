"""Generated from Smithy shape ``com.amazonaws.gamelift#ListComputeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.container_group_definition_name_or_arn
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.list_compute_input_status
    import aws_sdk_gamelift.types.location_string_model
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.positive_integer


class ListComputeInput(TypedDict, closed=True):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to retrieve compute resources for.</p>"""
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The name of a location to retrieve compute resources for. For an Amazon GameLift Servers Anywhere fleet, use a custom location. For a managed fleet, provide a Amazon Web Services Region or Local Zone code (for example: <code>us-west-2</code> or <code>us-west-2-lax-1</code>).</p>"""
    container_group_definition_name: NotRequired[
        "aws_sdk_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
    ]
    """<p>For computes in a managed container fleet, the name of the deployed container group definition. </p>"""
    compute_status: NotRequired[
        "aws_sdk_gamelift.types.list_compute_input_status.ListComputeInputStatus"
    ]
    """<p>The status of computes in a managed container fleet, based on the success of the latest update deployment.</p> <ul> <li> <p> <code>ACTIVE</code> -- The compute is deployed with the correct container definitions. It is ready to process game servers and host game sessions.</p> </li> <li> <p> <code>IMPAIRED</code> -- An update deployment to the compute failed, and the compute is deployed with incorrect container definitions.</p> </li> </ul>"""
    limit: NotRequired["aws_sdk_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComputeInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "location" in value:
        out["Location"] = value["location"]
    if "container_group_definition_name" in value:
        out["ContainerGroupDefinitionName"] = value["container_group_definition_name"]
    if "compute_status" in value:
        import aws_sdk_gamelift.types.list_compute_input_status

        out["ComputeStatus"] = (
            aws_sdk_gamelift.types.list_compute_input_status.serialize_aws_json_1_1(
                value["compute_status"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComputeInput:
    out: ListComputeInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "ContainerGroupDefinitionName" in data:
        out["container_group_definition_name"] = data["ContainerGroupDefinitionName"]
    if "ComputeStatus" in data:
        import aws_sdk_gamelift.types.list_compute_input_status

        out["compute_status"] = (
            aws_sdk_gamelift.types.list_compute_input_status.deserialize_aws_json_1_1(
                data["ComputeStatus"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
