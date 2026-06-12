"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_details
    import aws_sdk_securityhub.types.aws_guard_duty_detector_features_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsGuardDutyDetectorDetails(TypedDict):
    data_sources: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_details.AwsGuardDutyDetectorDataSourcesDetails"
    ]
    """<p> Describes which data sources are activated for the detector. </p>"""
    features: NotRequired[
        "aws_sdk_securityhub.types.aws_guard_duty_detector_features_list.AwsGuardDutyDetectorFeaturesList"
    ]
    """<p> Describes which features are activated for the detector. </p>"""
    finding_publishing_frequency: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The publishing frequency of the finding. </p>"""
    service_role: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The GuardDuty service role. </p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The activation status of the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorDetails) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_details

        out["DataSources"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_details.serialize_json(
                value["data_sources"]
            )
        )
    if "features" in value:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_features_list

        out["Features"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_features_list.serialize_json(
                value["features"]
            )
        )
    if "finding_publishing_frequency" in value:
        out["FindingPublishingFrequency"] = value["finding_publishing_frequency"]
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsGuardDutyDetectorDetails:
    out: AwsGuardDutyDetectorDetails = {}  # type: ignore[typeddict-item]
    if "DataSources" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_details

        out["data_sources"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_data_sources_details.deserialize_json(
                data["DataSources"]
            )
        )
    if "Features" in data:
        import aws_sdk_securityhub.types.aws_guard_duty_detector_features_list

        out["features"] = (
            aws_sdk_securityhub.types.aws_guard_duty_detector_features_list.deserialize_json(
                data["Features"]
            )
        )
    if "FindingPublishingFrequency" in data:
        out["finding_publishing_frequency"] = data["FindingPublishingFrequency"]
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
