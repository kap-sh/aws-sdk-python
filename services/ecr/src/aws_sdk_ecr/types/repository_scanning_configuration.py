"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryScanningConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.arn
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.scan_frequency
    import aws_sdk_ecr.types.scan_on_push_flag
    import aws_sdk_ecr.types.scanning_repository_filter_list


class RepositoryScanningConfiguration(TypedDict):
    repository_arn: NotRequired["aws_sdk_ecr.types.arn.Arn"]
    """<p>The ARN of the repository.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository.</p>"""
    scan_on_push: "aws_sdk_ecr.types.scan_on_push_flag.ScanOnPushFlag"
    """<p>Whether or not scan on push is configured for the repository.</p>"""
    scan_frequency: NotRequired["aws_sdk_ecr.types.scan_frequency.ScanFrequency"]
    """<p>The scan frequency for the repository.</p>"""
    applied_scan_filters: NotRequired[
        "aws_sdk_ecr.types.scanning_repository_filter_list.ScanningRepositoryFilterList"
    ]
    """<p>The scan filters applied to the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryScanningConfiguration) -> dict:
    out: dict = {}
    if "repository_arn" in value:
        out["repositoryArn"] = value["repository_arn"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    out["scanOnPush"] = value.get("scan_on_push", False)
    if "scan_frequency" in value:
        import aws_sdk_ecr.types.scan_frequency

        out["scanFrequency"] = aws_sdk_ecr.types.scan_frequency.serialize_aws_json_1_1(
            value["scan_frequency"]
        )
    if "applied_scan_filters" in value:
        import aws_sdk_ecr.types.scanning_repository_filter_list

        out["appliedScanFilters"] = (
            aws_sdk_ecr.types.scanning_repository_filter_list.serialize_aws_json_1_1(
                value["applied_scan_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryScanningConfiguration:
    out: RepositoryScanningConfiguration = {}  # type: ignore[typeddict-item]
    if "repositoryArn" in data:
        out["repository_arn"] = data["repositoryArn"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "scanOnPush" in data:
        out["scan_on_push"] = data["scanOnPush"]
    else:
        out["scan_on_push"] = False
    if "scanFrequency" in data:
        import aws_sdk_ecr.types.scan_frequency

        out["scan_frequency"] = (
            aws_sdk_ecr.types.scan_frequency.deserialize_aws_json_1_1(
                data["scanFrequency"]
            )
        )
    if "appliedScanFilters" in data:
        import aws_sdk_ecr.types.scanning_repository_filter_list

        out["applied_scan_filters"] = (
            aws_sdk_ecr.types.scanning_repository_filter_list.deserialize_aws_json_1_1(
                data["appliedScanFilters"]
            )
        )
    return out
