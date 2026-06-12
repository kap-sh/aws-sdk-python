"""Generated from Smithy shape ``com.amazonaws.ecr#ListImageReferrersFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.artifact_status_filter
    import aws_sdk_ecr.types.artifact_type_list


class ListImageReferrersFilter(TypedDict):
    artifact_types: NotRequired["aws_sdk_ecr.types.artifact_type_list.ArtifactTypeList"]
    """<p>The artifact types with which to filter your <a>ListImageReferrers</a> results.</p>"""
    artifact_status: NotRequired[
        "aws_sdk_ecr.types.artifact_status_filter.ArtifactStatusFilter"
    ]
    """<p>The artifact status with which to filter your <a>ListImageReferrers</a> results. Valid values are <code>ACTIVE</code>, <code>ARCHIVED</code>, <code>ACTIVATING</code>, or <code>ANY</code>. If not specified, only artifacts with <code>ACTIVE</code> status are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImageReferrersFilter) -> dict:
    out: dict = {}
    if "artifact_types" in value:
        import aws_sdk_ecr.types.artifact_type_list

        out["artifactTypes"] = (
            aws_sdk_ecr.types.artifact_type_list.serialize_aws_json_1_1(
                value["artifact_types"]
            )
        )
    if "artifact_status" in value:
        import aws_sdk_ecr.types.artifact_status_filter

        out["artifactStatus"] = (
            aws_sdk_ecr.types.artifact_status_filter.serialize_aws_json_1_1(
                value["artifact_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImageReferrersFilter:
    out: ListImageReferrersFilter = {}  # type: ignore[typeddict-item]
    if "artifactTypes" in data:
        import aws_sdk_ecr.types.artifact_type_list

        out["artifact_types"] = (
            aws_sdk_ecr.types.artifact_type_list.deserialize_aws_json_1_1(
                data["artifactTypes"]
            )
        )
    if "artifactStatus" in data:
        import aws_sdk_ecr.types.artifact_status_filter

        out["artifact_status"] = (
            aws_sdk_ecr.types.artifact_status_filter.deserialize_aws_json_1_1(
                data["artifactStatus"]
            )
        )
    return out
