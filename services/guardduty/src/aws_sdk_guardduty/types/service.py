"""Generated from Smithy shape ``com.amazonaws.guardduty#Service``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.action
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.detection
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.ebs_volume_scan_details
    import aws_sdk_guardduty.types.evidence
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.malware_scan_details
    import aws_sdk_guardduty.types.runtime_details
    import aws_sdk_guardduty.types.service_additional_info
    import aws_sdk_guardduty.types.string


class Service(TypedDict, closed=True):
    action: NotRequired["aws_sdk_guardduty.types.action.Action"]
    """<p>Information about the activity that is described in a finding.</p>"""
    evidence: NotRequired["aws_sdk_guardduty.types.evidence.Evidence"]
    """<p>An evidence object associated with the service.</p>"""
    archived: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether this finding is archived.</p>"""
    count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The total count of the occurrences of this finding type.</p>"""
    detector_id: NotRequired["aws_sdk_guardduty.types.detector_id.DetectorId"]
    """<p>The detector ID for the GuardDuty service.</p>"""
    event_first_seen: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The first-seen timestamp of the activity that prompted GuardDuty to generate this finding.</p>"""
    event_last_seen: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The last-seen timestamp of the activity that prompted GuardDuty to generate this finding.</p>"""
    resource_role: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The resource role information for this finding.</p>"""
    service_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the Amazon Web Services service (GuardDuty) that generated a finding.</p>"""
    user_feedback: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Feedback that was submitted about the finding.</p>"""
    additional_info: NotRequired[
        "aws_sdk_guardduty.types.service_additional_info.ServiceAdditionalInfo"
    ]
    """<p>Contains additional information about the generated finding.</p>"""
    feature_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the feature that generated a finding.</p>"""
    ebs_volume_scan_details: NotRequired[
        "aws_sdk_guardduty.types.ebs_volume_scan_details.EbsVolumeScanDetails"
    ]
    """<p>Returns details from the malware scan that created a finding.</p>"""
    runtime_details: NotRequired[
        "aws_sdk_guardduty.types.runtime_details.RuntimeDetails"
    ]
    """<p>Information about the process and any required context values for a specific finding</p>"""
    detection: NotRequired["aws_sdk_guardduty.types.detection.Detection"]
    """<p>Contains information about the detected unusual behavior.</p>"""
    malware_scan_details: NotRequired[
        "aws_sdk_guardduty.types.malware_scan_details.MalwareScanDetails"
    ]
    """<p>Returns details from the malware scan that generated a GuardDuty finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Service) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_guardduty.types.action

        out["action"] = aws_sdk_guardduty.types.action.serialize_json(value["action"])
    if "evidence" in value:
        import aws_sdk_guardduty.types.evidence

        out["evidence"] = aws_sdk_guardduty.types.evidence.serialize_json(
            value["evidence"]
        )
    if "archived" in value:
        out["archived"] = value["archived"]
    if "count" in value:
        out["count"] = value["count"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "event_first_seen" in value:
        out["eventFirstSeen"] = value["event_first_seen"]
    if "event_last_seen" in value:
        out["eventLastSeen"] = value["event_last_seen"]
    if "resource_role" in value:
        out["resourceRole"] = value["resource_role"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "user_feedback" in value:
        out["userFeedback"] = value["user_feedback"]
    if "additional_info" in value:
        import aws_sdk_guardduty.types.service_additional_info

        out["additionalInfo"] = (
            aws_sdk_guardduty.types.service_additional_info.serialize_json(
                value["additional_info"]
            )
        )
    if "feature_name" in value:
        out["featureName"] = value["feature_name"]
    if "ebs_volume_scan_details" in value:
        import aws_sdk_guardduty.types.ebs_volume_scan_details

        out["ebsVolumeScanDetails"] = (
            aws_sdk_guardduty.types.ebs_volume_scan_details.serialize_json(
                value["ebs_volume_scan_details"]
            )
        )
    if "runtime_details" in value:
        import aws_sdk_guardduty.types.runtime_details

        out["runtimeDetails"] = aws_sdk_guardduty.types.runtime_details.serialize_json(
            value["runtime_details"]
        )
    if "detection" in value:
        import aws_sdk_guardduty.types.detection

        out["detection"] = aws_sdk_guardduty.types.detection.serialize_json(
            value["detection"]
        )
    if "malware_scan_details" in value:
        import aws_sdk_guardduty.types.malware_scan_details

        out["malwareScanDetails"] = (
            aws_sdk_guardduty.types.malware_scan_details.serialize_json(
                value["malware_scan_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_guardduty.types.action

        out["action"] = aws_sdk_guardduty.types.action.deserialize_json(data["action"])
    if "evidence" in data:
        import aws_sdk_guardduty.types.evidence

        out["evidence"] = aws_sdk_guardduty.types.evidence.deserialize_json(
            data["evidence"]
        )
    if "archived" in data:
        out["archived"] = data["archived"]
    if "count" in data:
        out["count"] = data["count"]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "eventFirstSeen" in data:
        out["event_first_seen"] = data["eventFirstSeen"]
    if "eventLastSeen" in data:
        out["event_last_seen"] = data["eventLastSeen"]
    if "resourceRole" in data:
        out["resource_role"] = data["resourceRole"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "userFeedback" in data:
        out["user_feedback"] = data["userFeedback"]
    if "additionalInfo" in data:
        import aws_sdk_guardduty.types.service_additional_info

        out["additional_info"] = (
            aws_sdk_guardduty.types.service_additional_info.deserialize_json(
                data["additionalInfo"]
            )
        )
    if "featureName" in data:
        out["feature_name"] = data["featureName"]
    if "ebsVolumeScanDetails" in data:
        import aws_sdk_guardduty.types.ebs_volume_scan_details

        out["ebs_volume_scan_details"] = (
            aws_sdk_guardduty.types.ebs_volume_scan_details.deserialize_json(
                data["ebsVolumeScanDetails"]
            )
        )
    if "runtimeDetails" in data:
        import aws_sdk_guardduty.types.runtime_details

        out["runtime_details"] = (
            aws_sdk_guardduty.types.runtime_details.deserialize_json(
                data["runtimeDetails"]
            )
        )
    if "detection" in data:
        import aws_sdk_guardduty.types.detection

        out["detection"] = aws_sdk_guardduty.types.detection.deserialize_json(
            data["detection"]
        )
    if "malwareScanDetails" in data:
        import aws_sdk_guardduty.types.malware_scan_details

        out["malware_scan_details"] = (
            aws_sdk_guardduty.types.malware_scan_details.deserialize_json(
                data["malwareScanDetails"]
            )
        )
    return out
