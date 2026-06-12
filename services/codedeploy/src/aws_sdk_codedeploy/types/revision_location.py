"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.app_spec_content
    import aws_sdk_codedeploy.types.git_hub_location
    import aws_sdk_codedeploy.types.raw_string
    import aws_sdk_codedeploy.types.revision_location_type
    import aws_sdk_codedeploy.types.s3_location


class RevisionLocation(TypedDict):
    revision_type: NotRequired[
        "aws_sdk_codedeploy.types.revision_location_type.RevisionLocationType"
    ]
    """<p>The type of application revision:</p> <ul> <li> <p>S3: An application revision stored in Amazon S3.</p> </li> <li> <p>GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).</p> </li> <li> <p>String: A YAML-formatted or JSON-formatted string (Lambda deployments only).</p> </li> <li> <p>AppSpecContent: An <code>AppSpecContent</code> object that contains the contents of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.</p> </li> </ul>"""
    s3_location: NotRequired["aws_sdk_codedeploy.types.s3_location.S3Location"]
    """<p>Information about the location of a revision stored in Amazon S3. </p>"""
    git_hub_location: NotRequired[
        "aws_sdk_codedeploy.types.git_hub_location.GitHubLocation"
    ]
    """<p>Information about the location of application artifacts stored in GitHub.</p>"""
    string: NotRequired["aws_sdk_codedeploy.types.raw_string.RawString"]
    """<p>Information about the location of an Lambda deployment revision stored as a RawString.</p>"""
    app_spec_content: NotRequired[
        "aws_sdk_codedeploy.types.app_spec_content.AppSpecContent"
    ]
    """<p> The content of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionLocation) -> dict:
    out: dict = {}
    if "revision_type" in value:
        import aws_sdk_codedeploy.types.revision_location_type

        out["revisionType"] = (
            aws_sdk_codedeploy.types.revision_location_type.serialize_aws_json_1_1(
                value["revision_type"]
            )
        )
    if "s3_location" in value:
        import aws_sdk_codedeploy.types.s3_location

        out["s3Location"] = aws_sdk_codedeploy.types.s3_location.serialize_aws_json_1_1(
            value["s3_location"]
        )
    if "git_hub_location" in value:
        import aws_sdk_codedeploy.types.git_hub_location

        out["gitHubLocation"] = (
            aws_sdk_codedeploy.types.git_hub_location.serialize_aws_json_1_1(
                value["git_hub_location"]
            )
        )
    if "string" in value:
        import aws_sdk_codedeploy.types.raw_string

        out["string"] = aws_sdk_codedeploy.types.raw_string.serialize_aws_json_1_1(
            value["string"]
        )
    if "app_spec_content" in value:
        import aws_sdk_codedeploy.types.app_spec_content

        out["appSpecContent"] = (
            aws_sdk_codedeploy.types.app_spec_content.serialize_aws_json_1_1(
                value["app_spec_content"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevisionLocation:
    out: RevisionLocation = {}  # type: ignore[typeddict-item]
    if "revisionType" in data:
        import aws_sdk_codedeploy.types.revision_location_type

        out["revision_type"] = (
            aws_sdk_codedeploy.types.revision_location_type.deserialize_aws_json_1_1(
                data["revisionType"]
            )
        )
    if "s3Location" in data:
        import aws_sdk_codedeploy.types.s3_location

        out["s3_location"] = (
            aws_sdk_codedeploy.types.s3_location.deserialize_aws_json_1_1(
                data["s3Location"]
            )
        )
    if "gitHubLocation" in data:
        import aws_sdk_codedeploy.types.git_hub_location

        out["git_hub_location"] = (
            aws_sdk_codedeploy.types.git_hub_location.deserialize_aws_json_1_1(
                data["gitHubLocation"]
            )
        )
    if "string" in data:
        import aws_sdk_codedeploy.types.raw_string

        out["string"] = aws_sdk_codedeploy.types.raw_string.deserialize_aws_json_1_1(
            data["string"]
        )
    if "appSpecContent" in data:
        import aws_sdk_codedeploy.types.app_spec_content

        out["app_spec_content"] = (
            aws_sdk_codedeploy.types.app_spec_content.deserialize_aws_json_1_1(
                data["appSpecContent"]
            )
        )
    return out
