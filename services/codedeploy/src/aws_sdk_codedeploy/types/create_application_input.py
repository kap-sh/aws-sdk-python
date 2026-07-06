"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.compute_platform
    import aws_sdk_codedeploy.types.tag_list


class CreateApplicationInput(TypedDict, closed=True):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p>The name of the application. This name must be unique with the applicable user or Amazon Web Services account.</p>"""
    compute_platform: NotRequired[
        "aws_sdk_codedeploy.types.compute_platform.ComputePlatform"
    ]
    """<p> The destination platform type for the deployment (<code>Lambda</code>, <code>Server</code>, or <code>ECS</code>).</p>"""
    tags: NotRequired["aws_sdk_codedeploy.types.tag_list.TagList"]
    """<p> The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    if "compute_platform" in value:
        import aws_sdk_codedeploy.types.compute_platform

        out["computePlatform"] = (
            aws_sdk_codedeploy.types.compute_platform.serialize_aws_json_1_1(
                value["compute_platform"]
            )
        )
    if "tags" in value:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationInput:
    out: CreateApplicationInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError("CreateApplicationInput.application_name required")
    if "computePlatform" in data:
        import aws_sdk_codedeploy.types.compute_platform

        out["compute_platform"] = (
            aws_sdk_codedeploy.types.compute_platform.deserialize_aws_json_1_1(
                data["computePlatform"]
            )
        )
    if "tags" in data:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
