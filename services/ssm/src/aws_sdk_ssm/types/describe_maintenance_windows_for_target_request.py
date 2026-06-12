"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowsForTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_resource_type
    import aws_sdk_ssm.types.maintenance_window_search_max_results
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.targets


class DescribeMaintenanceWindowsForTargetRequest(TypedDict):
    targets: "aws_sdk_ssm.types.targets.Targets"
    """<p>The managed node ID or key-value pair to retrieve information about.</p>"""
    resource_type: "aws_sdk_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
    """<p>The type of resource you want to retrieve information about. For example, <code>INSTANCE</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_search_max_results.MaintenanceWindowSearchMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowsForTargetRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.targets

    out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    import aws_sdk_ssm.types.maintenance_window_resource_type

    out["ResourceType"] = (
        aws_sdk_ssm.types.maintenance_window_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowsForTargetRequest:
    out: DescribeMaintenanceWindowsForTargetRequest = {}  # type: ignore[typeddict-item]
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    else:
        raise DeserializationError(
            "DescribeMaintenanceWindowsForTargetRequest.targets required"
        )
    if "ResourceType" in data:
        import aws_sdk_ssm.types.maintenance_window_resource_type

        out["resource_type"] = (
            aws_sdk_ssm.types.maintenance_window_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeMaintenanceWindowsForTargetRequest.resource_type required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
