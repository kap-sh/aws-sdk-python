"""Generated from Smithy shape ``com.amazonaws.rum#PutRumEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rum.types.alias
    import aws_sdk_rum.types.app_monitor_details
    import aws_sdk_rum.types.app_monitor_id
    import aws_sdk_rum.types.rum_event_list
    import aws_sdk_rum.types.user_details


class PutRumEventsRequest(TypedDict):
    id: "aws_sdk_rum.types.app_monitor_id.AppMonitorId"
    """<p>The ID of the app monitor that is sending this data.</p>"""
    batch_id: "str"
    """<p>A unique identifier for this batch of RUM event data.</p>"""
    app_monitor_details: "aws_sdk_rum.types.app_monitor_details.AppMonitorDetails"
    """<p>A structure that contains information about the app monitor that collected this telemetry information.</p>"""
    user_details: "aws_sdk_rum.types.user_details.UserDetails"
    """<p>A structure that contains information about the user session that this batch of events was collected from.</p>"""
    rum_events: "aws_sdk_rum.types.rum_event_list.RumEventList"
    """<p>An array of structures that contain the telemetry event data.</p>"""
    alias: NotRequired["aws_sdk_rum.types.alias.Alias"]
    r"""<p>If the app monitor uses a resource-based policy that requires <code>PutRumEvents</code> requests to specify a certain alias, specify that alias here. This alias will be compared to the <code>rum:alias</code> context key in the resource-based policy. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html\">Using resource-based policies with CloudWatch RUM</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRumEventsRequest) -> dict:
    out: dict = {}
    out["BatchId"] = value["batch_id"]
    import aws_sdk_rum.types.app_monitor_details

    out["AppMonitorDetails"] = aws_sdk_rum.types.app_monitor_details.serialize_json(
        value["app_monitor_details"]
    )
    import aws_sdk_rum.types.user_details

    out["UserDetails"] = aws_sdk_rum.types.user_details.serialize_json(
        value["user_details"]
    )
    import aws_sdk_rum.types.rum_event_list

    out["RumEvents"] = aws_sdk_rum.types.rum_event_list.serialize_json(
        value["rum_events"]
    )
    if "alias" in value:
        out["Alias"] = value["alias"]
    return out


def deserialize_json(data: dict) -> PutRumEventsRequest:
    out: PutRumEventsRequest = {}  # type: ignore[typeddict-item]
    if "BatchId" in data:
        out["batch_id"] = data["BatchId"]
    else:
        raise DeserializationError("PutRumEventsRequest.batch_id required")
    if "AppMonitorDetails" in data:
        import aws_sdk_rum.types.app_monitor_details

        out["app_monitor_details"] = (
            aws_sdk_rum.types.app_monitor_details.deserialize_json(
                data["AppMonitorDetails"]
            )
        )
    else:
        raise DeserializationError("PutRumEventsRequest.app_monitor_details required")
    if "UserDetails" in data:
        import aws_sdk_rum.types.user_details

        out["user_details"] = aws_sdk_rum.types.user_details.deserialize_json(
            data["UserDetails"]
        )
    else:
        raise DeserializationError("PutRumEventsRequest.user_details required")
    if "RumEvents" in data:
        import aws_sdk_rum.types.rum_event_list

        out["rum_events"] = aws_sdk_rum.types.rum_event_list.deserialize_json(
            data["RumEvents"]
        )
    else:
        raise DeserializationError("PutRumEventsRequest.rum_events required")
    if "Alias" in data:
        out["alias"] = data["Alias"]
    return out
