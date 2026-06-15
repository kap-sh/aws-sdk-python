"""Generated from Smithy shape ``com.amazonaws.emr#DescribeReleaseLabelOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.os_release_list
    import aws_sdk_emr.types.simplified_application_list
    import aws_sdk_emr.types.string


class DescribeReleaseLabelOutput(TypedDict):
    release_label: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The target release label described in the response.</p>"""
    applications: NotRequired[
        "aws_sdk_emr.types.simplified_application_list.SimplifiedApplicationList"
    ]
    """<p>The list of applications available for the target release label. <code>Name</code> is the name of the application. <code>Version</code> is the concise version of the application.</p>"""
    next_token: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The pagination token. Reserved for future use. Currently set to null.</p>"""
    available_os_releases: NotRequired[
        "aws_sdk_emr.types.os_release_list.OSReleaseList"
    ]
    r"""<p>The list of available Amazon Linux release versions for an Amazon EMR release. Contains a Label field that is formatted as shown in <a href=\"https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-al2.html\"> <i>Amazon Linux 2 Release Notes</i> </a>. For example, <a href=\"https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20220218.html\">2.0.20220218.1</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReleaseLabelOutput) -> dict:
    out: dict = {}
    if "release_label" in value:
        out["ReleaseLabel"] = value["release_label"]
    if "applications" in value:
        import aws_sdk_emr.types.simplified_application_list

        out["Applications"] = (
            aws_sdk_emr.types.simplified_application_list.serialize_aws_json_1_1(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "available_os_releases" in value:
        import aws_sdk_emr.types.os_release_list

        out["AvailableOSReleases"] = (
            aws_sdk_emr.types.os_release_list.serialize_aws_json_1_1(
                value["available_os_releases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReleaseLabelOutput:
    out: DescribeReleaseLabelOutput = {}  # type: ignore[typeddict-item]
    if "ReleaseLabel" in data:
        out["release_label"] = data["ReleaseLabel"]
    if "Applications" in data:
        import aws_sdk_emr.types.simplified_application_list

        out["applications"] = (
            aws_sdk_emr.types.simplified_application_list.deserialize_aws_json_1_1(
                data["Applications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AvailableOSReleases" in data:
        import aws_sdk_emr.types.os_release_list

        out["available_os_releases"] = (
            aws_sdk_emr.types.os_release_list.deserialize_aws_json_1_1(
                data["AvailableOSReleases"]
            )
        )
    return out
