"""Generated from Smithy shape ``com.amazonaws.xray#TraceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.annotations
    import capo_xray.types.error_root_causes
    import capo_xray.types.fault_root_causes
    import capo_xray.types.http
    import capo_xray.types.integer
    import capo_xray.types.nullable_boolean
    import capo_xray.types.nullable_double
    import capo_xray.types.response_time_root_causes
    import capo_xray.types.service_id
    import capo_xray.types.service_ids
    import capo_xray.types.timestamp
    import capo_xray.types.trace_availability_zones
    import capo_xray.types.trace_id
    import capo_xray.types.trace_instance_ids
    import capo_xray.types.trace_resource_ar_ns
    import capo_xray.types.trace_users


class TraceSummary(TypedDict, closed=True):
    id: NotRequired["capo_xray.types.trace_id.TraceId"]
    """<p>The unique identifier for the request that generated the trace's segments and subsegments.</p>"""
    start_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The start time of a trace, based on the earliest trace segment start time.</p>"""
    duration: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p> The length of time in seconds between the start time of the earliest segment that started and the end time of the last segment that completed.</p>"""
    response_time: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p>The length of time in seconds between the start and end times of the root segment. If the service performs work asynchronously, the response time measures the time before the response is sent to the user, while the duration measures the amount of time before the last traced activity completes.</p>"""
    has_fault: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>The root segment document has a 500 series error.</p>"""
    has_error: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>The root segment document has a 400 series error.</p>"""
    has_throttle: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>One or more of the segment documents has a 429 throttling error.</p>"""
    is_partial: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>One or more of the segment documents is in progress.</p>"""
    http: NotRequired["capo_xray.types.http.Http"]
    """<p>Information about the HTTP request served by the trace.</p>"""
    annotations: NotRequired["capo_xray.types.annotations.Annotations"]
    """<p>Annotations from the trace's segment documents.</p>"""
    users: NotRequired["capo_xray.types.trace_users.TraceUsers"]
    """<p>Users from the trace's segment documents.</p>"""
    service_ids: NotRequired["capo_xray.types.service_ids.ServiceIds"]
    """<p>Service IDs from the trace's segment documents.</p>"""
    resource_ar_ns: NotRequired[
        "capo_xray.types.trace_resource_ar_ns.TraceResourceARNs"
    ]
    """<p>A list of resource ARNs for any resource corresponding to the trace segments.</p>"""
    instance_ids: NotRequired["capo_xray.types.trace_instance_ids.TraceInstanceIds"]
    """<p>A list of EC2 instance IDs for any instance corresponding to the trace segments.</p>"""
    availability_zones: NotRequired[
        "capo_xray.types.trace_availability_zones.TraceAvailabilityZones"
    ]
    """<p>A list of Availability Zones for any zone corresponding to the trace segments.</p>"""
    entry_point: NotRequired["capo_xray.types.service_id.ServiceId"]
    """<p>The root of a trace.</p>"""
    fault_root_causes: NotRequired["capo_xray.types.fault_root_causes.FaultRootCauses"]
    """<p>A collection of FaultRootCause structures corresponding to the trace segments.</p>"""
    error_root_causes: NotRequired["capo_xray.types.error_root_causes.ErrorRootCauses"]
    """<p>A collection of ErrorRootCause structures corresponding to the trace segments.</p>"""
    response_time_root_causes: NotRequired[
        "capo_xray.types.response_time_root_causes.ResponseTimeRootCauses"
    ]
    """<p>A collection of ResponseTimeRootCause structures corresponding to the trace segments.</p>"""
    revision: "capo_xray.types.integer.Integer"
    """<p>The revision number of a trace.</p>"""
    matched_event_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The matched time stamp of a defined event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "start_time" in value:
        import capo_xray.types.timestamp

        out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "response_time" in value:
        out["ResponseTime"] = value["response_time"]
    if "has_fault" in value:
        out["HasFault"] = value["has_fault"]
    if "has_error" in value:
        out["HasError"] = value["has_error"]
    if "has_throttle" in value:
        out["HasThrottle"] = value["has_throttle"]
    if "is_partial" in value:
        out["IsPartial"] = value["is_partial"]
    if "http" in value:
        import capo_xray.types.http

        out["Http"] = capo_xray.types.http.serialize_json(value["http"])
    if "annotations" in value:
        import capo_xray.types.annotations

        out["Annotations"] = capo_xray.types.annotations.serialize_json(
            value["annotations"]
        )
    if "users" in value:
        import capo_xray.types.trace_users

        out["Users"] = capo_xray.types.trace_users.serialize_json(value["users"])
    if "service_ids" in value:
        import capo_xray.types.service_ids

        out["ServiceIds"] = capo_xray.types.service_ids.serialize_json(
            value["service_ids"]
        )
    if "resource_ar_ns" in value:
        import capo_xray.types.trace_resource_ar_ns

        out["ResourceARNs"] = capo_xray.types.trace_resource_ar_ns.serialize_json(
            value["resource_ar_ns"]
        )
    if "instance_ids" in value:
        import capo_xray.types.trace_instance_ids

        out["InstanceIds"] = capo_xray.types.trace_instance_ids.serialize_json(
            value["instance_ids"]
        )
    if "availability_zones" in value:
        import capo_xray.types.trace_availability_zones

        out["AvailabilityZones"] = (
            capo_xray.types.trace_availability_zones.serialize_json(
                value["availability_zones"]
            )
        )
    if "entry_point" in value:
        import capo_xray.types.service_id

        out["EntryPoint"] = capo_xray.types.service_id.serialize_json(
            value["entry_point"]
        )
    if "fault_root_causes" in value:
        import capo_xray.types.fault_root_causes

        out["FaultRootCauses"] = capo_xray.types.fault_root_causes.serialize_json(
            value["fault_root_causes"]
        )
    if "error_root_causes" in value:
        import capo_xray.types.error_root_causes

        out["ErrorRootCauses"] = capo_xray.types.error_root_causes.serialize_json(
            value["error_root_causes"]
        )
    if "response_time_root_causes" in value:
        import capo_xray.types.response_time_root_causes

        out["ResponseTimeRootCauses"] = (
            capo_xray.types.response_time_root_causes.serialize_json(
                value["response_time_root_causes"]
            )
        )
    out["Revision"] = value.get("revision", 0)
    if "matched_event_time" in value:
        import capo_xray.types.timestamp

        out["MatchedEventTime"] = capo_xray.types.timestamp.serialize_json(
            value["matched_event_time"]
        )
    return out


def deserialize_json(data: dict) -> TraceSummary:
    out: TraceSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "StartTime" in data:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "ResponseTime" in data:
        out["response_time"] = data["ResponseTime"]
    if "HasFault" in data:
        out["has_fault"] = data["HasFault"]
    if "HasError" in data:
        out["has_error"] = data["HasError"]
    if "HasThrottle" in data:
        out["has_throttle"] = data["HasThrottle"]
    if "IsPartial" in data:
        out["is_partial"] = data["IsPartial"]
    if "Http" in data:
        import capo_xray.types.http

        out["http"] = capo_xray.types.http.deserialize_json(data["Http"])
    if "Annotations" in data:
        import capo_xray.types.annotations

        out["annotations"] = capo_xray.types.annotations.deserialize_json(
            data["Annotations"]
        )
    if "Users" in data:
        import capo_xray.types.trace_users

        out["users"] = capo_xray.types.trace_users.deserialize_json(data["Users"])
    if "ServiceIds" in data:
        import capo_xray.types.service_ids

        out["service_ids"] = capo_xray.types.service_ids.deserialize_json(
            data["ServiceIds"]
        )
    if "ResourceARNs" in data:
        import capo_xray.types.trace_resource_ar_ns

        out["resource_ar_ns"] = capo_xray.types.trace_resource_ar_ns.deserialize_json(
            data["ResourceARNs"]
        )
    if "InstanceIds" in data:
        import capo_xray.types.trace_instance_ids

        out["instance_ids"] = capo_xray.types.trace_instance_ids.deserialize_json(
            data["InstanceIds"]
        )
    if "AvailabilityZones" in data:
        import capo_xray.types.trace_availability_zones

        out["availability_zones"] = (
            capo_xray.types.trace_availability_zones.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if "EntryPoint" in data:
        import capo_xray.types.service_id

        out["entry_point"] = capo_xray.types.service_id.deserialize_json(
            data["EntryPoint"]
        )
    if "FaultRootCauses" in data:
        import capo_xray.types.fault_root_causes

        out["fault_root_causes"] = capo_xray.types.fault_root_causes.deserialize_json(
            data["FaultRootCauses"]
        )
    if "ErrorRootCauses" in data:
        import capo_xray.types.error_root_causes

        out["error_root_causes"] = capo_xray.types.error_root_causes.deserialize_json(
            data["ErrorRootCauses"]
        )
    if "ResponseTimeRootCauses" in data:
        import capo_xray.types.response_time_root_causes

        out["response_time_root_causes"] = (
            capo_xray.types.response_time_root_causes.deserialize_json(
                data["ResponseTimeRootCauses"]
            )
        )
    if "Revision" in data:
        out["revision"] = data["Revision"]
    else:
        out["revision"] = 0
    if "MatchedEventTime" in data:
        import capo_xray.types.timestamp

        out["matched_event_time"] = capo_xray.types.timestamp.deserialize_json(
            data["MatchedEventTime"]
        )
    return out
