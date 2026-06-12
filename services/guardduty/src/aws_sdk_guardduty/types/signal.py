"""Generated from Smithy shape ``com.amazonaws.guardduty#Signal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.actor_ids
    import aws_sdk_guardduty.types.double
    import aws_sdk_guardduty.types.endpoint_ids
    import aws_sdk_guardduty.types.indicators
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.resource_uids
    import aws_sdk_guardduty.types.signal_description
    import aws_sdk_guardduty.types.signal_type
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class Signal(TypedDict):
    uid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique identifier of the signal.</p>"""
    type: NotRequired["aws_sdk_guardduty.types.signal_type.SignalType"]
    """<p>The type of the signal used to identify an attack sequence.</p> <p>Signals can be GuardDuty findings or activities observed in data sources that GuardDuty monitors. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html\">Foundational data sources</a> in the <i>Amazon GuardDuty User Guide</i>.</p> <p>A signal type can be one of the valid values listed in this API. Here are the related descriptions:</p> <ul> <li> <p> <code>FINDING</code> - Individually generated GuardDuty finding.</p> </li> <li> <p> <code>CLOUD_TRAIL</code> - Activity observed from CloudTrail logs</p> </li> <li> <p> <code>S3_DATA_EVENTS</code> - Activity observed from CloudTrail data events for S3. Activities associated with this type will show up only when you have enabled GuardDuty S3 Protection feature in your account. For more information about S3 Protection and steps to enable it, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html\">S3 Protection</a> in the <i>Amazon GuardDuty User Guide</i>.</p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_guardduty.types.signal_description.SignalDescription"
    ]
    """<p>The description of the signal.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the signal. For example, when signal type is <code>FINDING</code>, the signal name is the name of the finding.</p>"""
    created_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the first finding or activity related to this signal was observed.</p>"""
    updated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when this signal was last observed.</p>"""
    first_seen_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the first finding or activity related to this signal was observed.</p>"""
    last_seen_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the last finding or activity related to this signal was observed.</p>"""
    severity: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The severity associated with the signal. For more information about severity, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html\">Findings severity levels</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""
    count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The number of times this signal was observed.</p>"""
    resource_uids: NotRequired["aws_sdk_guardduty.types.resource_uids.ResourceUids"]
    """<p>Information about the unique identifiers of the resources involved in the signal.</p>"""
    actor_ids: NotRequired["aws_sdk_guardduty.types.actor_ids.ActorIds"]
    """<p>Information about the IDs of the threat actors involved in the signal.</p>"""
    endpoint_ids: NotRequired["aws_sdk_guardduty.types.endpoint_ids.EndpointIds"]
    """<p>Information about the endpoint IDs associated with this signal.</p>"""
    signal_indicators: NotRequired["aws_sdk_guardduty.types.indicators.Indicators"]
    """<p>Contains information about the indicators associated with the signals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Signal) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "type" in value:
        import aws_sdk_guardduty.types.signal_type

        out["type"] = aws_sdk_guardduty.types.signal_type.serialize_json(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    if "created_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["createdAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["updatedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "first_seen_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["firstSeenAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["first_seen_at"]
        )
    if "last_seen_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["lastSeenAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["last_seen_at"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "count" in value:
        out["count"] = value["count"]
    if "resource_uids" in value:
        import aws_sdk_guardduty.types.resource_uids

        out["resourceUids"] = aws_sdk_guardduty.types.resource_uids.serialize_json(
            value["resource_uids"]
        )
    if "actor_ids" in value:
        import aws_sdk_guardduty.types.actor_ids

        out["actorIds"] = aws_sdk_guardduty.types.actor_ids.serialize_json(
            value["actor_ids"]
        )
    if "endpoint_ids" in value:
        import aws_sdk_guardduty.types.endpoint_ids

        out["endpointIds"] = aws_sdk_guardduty.types.endpoint_ids.serialize_json(
            value["endpoint_ids"]
        )
    if "signal_indicators" in value:
        import aws_sdk_guardduty.types.indicators

        out["signalIndicators"] = aws_sdk_guardduty.types.indicators.serialize_json(
            value["signal_indicators"]
        )
    return out


def deserialize_json(data: dict) -> Signal:
    out: Signal = {}  # type: ignore[typeddict-item]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "type" in data:
        import aws_sdk_guardduty.types.signal_type

        out["type"] = aws_sdk_guardduty.types.signal_type.deserialize_json(data["type"])
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    if "createdAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["created_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["updated_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "firstSeenAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["first_seen_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["firstSeenAt"]
        )
    if "lastSeenAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["last_seen_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["lastSeenAt"]
        )
    if "severity" in data:
        out["severity"] = data["severity"]
    if "count" in data:
        out["count"] = data["count"]
    if "resourceUids" in data:
        import aws_sdk_guardduty.types.resource_uids

        out["resource_uids"] = aws_sdk_guardduty.types.resource_uids.deserialize_json(
            data["resourceUids"]
        )
    if "actorIds" in data:
        import aws_sdk_guardduty.types.actor_ids

        out["actor_ids"] = aws_sdk_guardduty.types.actor_ids.deserialize_json(
            data["actorIds"]
        )
    if "endpointIds" in data:
        import aws_sdk_guardduty.types.endpoint_ids

        out["endpoint_ids"] = aws_sdk_guardduty.types.endpoint_ids.deserialize_json(
            data["endpointIds"]
        )
    if "signalIndicators" in data:
        import aws_sdk_guardduty.types.indicators

        out["signal_indicators"] = aws_sdk_guardduty.types.indicators.deserialize_json(
            data["signalIndicators"]
        )
    return out
