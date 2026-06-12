"""Generated from Smithy shape ``com.amazonaws.guardduty#GetDetectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.data_source_configurations_result
    import aws_sdk_guardduty.types.detector_feature_configurations_results
    import aws_sdk_guardduty.types.detector_status
    import aws_sdk_guardduty.types.finding_publishing_frequency
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tag_map


class GetDetectorResponse(TypedDict):
    created_at: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The timestamp of when the detector was created.</p>"""
    finding_publishing_frequency: NotRequired[
        "aws_sdk_guardduty.types.finding_publishing_frequency.FindingPublishingFrequency"
    ]
    """<p>The publishing frequency of the finding.</p>"""
    service_role: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The GuardDuty service role.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.detector_status.DetectorStatus"]
    """<p>The detector status.</p>"""
    updated_at: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The last-updated timestamp for the detector.</p>"""
    data_sources: NotRequired[
        "aws_sdk_guardduty.types.data_source_configurations_result.DataSourceConfigurationsResult"
    ]
    """<p>Describes which data sources are enabled for the detector.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tag_map.TagMap"]
    """<p>The tags of the detector resource.</p>"""
    features: NotRequired[
        "aws_sdk_guardduty.types.detector_feature_configurations_results.DetectorFeatureConfigurationsResults"
    ]
    """<p>Describes the features that have been enabled for the detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDetectorResponse) -> dict:
    out: dict = {}
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "finding_publishing_frequency" in value:
        import aws_sdk_guardduty.types.finding_publishing_frequency

        out["findingPublishingFrequency"] = (
            aws_sdk_guardduty.types.finding_publishing_frequency.serialize_json(
                value["finding_publishing_frequency"]
            )
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "status" in value:
        import aws_sdk_guardduty.types.detector_status

        out["status"] = aws_sdk_guardduty.types.detector_status.serialize_json(
            value["status"]
        )
    if "updated_at" in value:
        out["updatedAt"] = value["updated_at"]
    if "data_sources" in value:
        import aws_sdk_guardduty.types.data_source_configurations_result

        out["dataSources"] = (
            aws_sdk_guardduty.types.data_source_configurations_result.serialize_json(
                value["data_sources"]
            )
        )
    if "tags" in value:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.serialize_json(value["tags"])
    if "features" in value:
        import aws_sdk_guardduty.types.detector_feature_configurations_results

        out["features"] = (
            aws_sdk_guardduty.types.detector_feature_configurations_results.serialize_json(
                value["features"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDetectorResponse:
    out: GetDetectorResponse = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "findingPublishingFrequency" in data:
        import aws_sdk_guardduty.types.finding_publishing_frequency

        out["finding_publishing_frequency"] = (
            aws_sdk_guardduty.types.finding_publishing_frequency.deserialize_json(
                data["findingPublishingFrequency"]
            )
        )
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "status" in data:
        import aws_sdk_guardduty.types.detector_status

        out["status"] = aws_sdk_guardduty.types.detector_status.deserialize_json(
            data["status"]
        )
    if "updatedAt" in data:
        out["updated_at"] = data["updatedAt"]
    if "dataSources" in data:
        import aws_sdk_guardduty.types.data_source_configurations_result

        out["data_sources"] = (
            aws_sdk_guardduty.types.data_source_configurations_result.deserialize_json(
                data["dataSources"]
            )
        )
    if "tags" in data:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.deserialize_json(data["tags"])
    if "features" in data:
        import aws_sdk_guardduty.types.detector_feature_configurations_results

        out["features"] = (
            aws_sdk_guardduty.types.detector_feature_configurations_results.deserialize_json(
                data["features"]
            )
        )
    return out
