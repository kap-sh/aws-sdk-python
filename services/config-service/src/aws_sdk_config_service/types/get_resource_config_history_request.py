"""Generated from Smithy shape ``com.amazonaws.configservice#GetResourceConfigHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.chronological_order
    import aws_sdk_config_service.types.earlier_time
    import aws_sdk_config_service.types.later_time
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.resource_id
    import aws_sdk_config_service.types.resource_type


class GetResourceConfigHistoryRequest(TypedDict):
    resource_type: "aws_sdk_config_service.types.resource_type.ResourceType"
    """<p>The resource type.</p>"""
    resource_id: "aws_sdk_config_service.types.resource_id.ResourceId"
    """<p>The ID of the resource (for example., <code>sg-xxxxxx</code>).</p>"""
    later_time: NotRequired["aws_sdk_config_service.types.later_time.LaterTime"]
    """<p>The chronologically latest time in the time range for which the history requested. If not specified, current time is taken.</p>"""
    earlier_time: NotRequired["aws_sdk_config_service.types.earlier_time.EarlierTime"]
    """<p>The chronologically earliest time in the time range for which the history requested. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.</p>"""
    chronological_order: NotRequired[
        "aws_sdk_config_service.types.chronological_order.ChronologicalOrder"
    ]
    """<p>The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.</p>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of configuration items returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceConfigHistoryRequest) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.resource_type

    out["resourceType"] = (
        aws_sdk_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["resourceId"] = value["resource_id"]
    if "later_time" in value:
        import aws_sdk_config_service.types.later_time

        out["laterTime"] = (
            aws_sdk_config_service.types.later_time.serialize_aws_json_1_1(
                value["later_time"]
            )
        )
    if "earlier_time" in value:
        import aws_sdk_config_service.types.earlier_time

        out["earlierTime"] = (
            aws_sdk_config_service.types.earlier_time.serialize_aws_json_1_1(
                value["earlier_time"]
            )
        )
    if "chronological_order" in value:
        import aws_sdk_config_service.types.chronological_order

        out["chronologicalOrder"] = (
            aws_sdk_config_service.types.chronological_order.serialize_aws_json_1_1(
                value["chronological_order"]
            )
        )
    out["limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceConfigHistoryRequest:
    out: GetResourceConfigHistoryRequest = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_config_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "GetResourceConfigHistoryRequest.resource_type required"
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "GetResourceConfigHistoryRequest.resource_id required"
        )
    if "laterTime" in data:
        import aws_sdk_config_service.types.later_time

        out["later_time"] = (
            aws_sdk_config_service.types.later_time.deserialize_aws_json_1_1(
                data["laterTime"]
            )
        )
    if "earlierTime" in data:
        import aws_sdk_config_service.types.earlier_time

        out["earlier_time"] = (
            aws_sdk_config_service.types.earlier_time.deserialize_aws_json_1_1(
                data["earlierTime"]
            )
        )
    if "chronologicalOrder" in data:
        import aws_sdk_config_service.types.chronological_order

        out["chronological_order"] = (
            aws_sdk_config_service.types.chronological_order.deserialize_aws_json_1_1(
                data["chronologicalOrder"]
            )
        )
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
