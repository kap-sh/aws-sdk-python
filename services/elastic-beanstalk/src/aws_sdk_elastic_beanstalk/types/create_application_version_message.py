"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreateApplicationVersionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.application_version_proccess
    import aws_sdk_elastic_beanstalk.types.auto_create_application
    import aws_sdk_elastic_beanstalk.types.build_configuration
    import aws_sdk_elastic_beanstalk.types.description
    import aws_sdk_elastic_beanstalk.types.s3_location
    import aws_sdk_elastic_beanstalk.types.source_build_information
    import aws_sdk_elastic_beanstalk.types.tags
    import aws_sdk_elastic_beanstalk.types.version_label


class CreateApplicationVersionMessage(TypedDict, closed=True):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p> The name of the application. If no application is found with this name, and <code>AutoCreateApplication</code> is <code>false</code>, returns an <code>InvalidParameterValue</code> error. </p>"""
    version_label: "aws_sdk_elastic_beanstalk.types.version_label.VersionLabel"
    """<p>A label identifying this version.</p> <p>Constraint: Must be unique per application. If an application version already exists with this label for the specified application, AWS Elastic Beanstalk returns an <code>InvalidParameterValue</code> error. </p>"""
    description: NotRequired["aws_sdk_elastic_beanstalk.types.description.Description"]
    """<p>A description of this application version.</p>"""
    source_build_information: NotRequired[
        "aws_sdk_elastic_beanstalk.types.source_build_information.SourceBuildInformation"
    ]
    """<p>Specify a commit in an AWS CodeCommit Git repository to use as the source code for the application version.</p>"""
    source_bundle: NotRequired["aws_sdk_elastic_beanstalk.types.s3_location.S3Location"]
    """<p>The Amazon S3 bucket and key that identify the location of the source bundle for this version.</p> <note> <p>The Amazon S3 bucket must be in the same region as the environment.</p> </note> <p>Specify a source bundle in S3 or a commit in an AWS CodeCommit repository (with <code>SourceBuildInformation</code>), but not both. If neither <code>SourceBundle</code> nor <code>SourceBuildInformation</code> are provided, Elastic Beanstalk uses a sample application.</p>"""
    build_configuration: NotRequired[
        "aws_sdk_elastic_beanstalk.types.build_configuration.BuildConfiguration"
    ]
    """<p>Settings for an AWS CodeBuild build.</p>"""
    auto_create_application: NotRequired[
        "aws_sdk_elastic_beanstalk.types.auto_create_application.AutoCreateApplication"
    ]
    """<p>Set to <code>true</code> to create an application with the specified name if it doesn't already exist.</p>"""
    process: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_version_proccess.ApplicationVersionProccess"
    ]
    """<p>Pre-processes and validates the environment manifest (<code>env.yaml</code>) and configuration files (<code>*.config</code> files in the <code>.ebextensions</code> folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.</p> <p>You must turn processing on for application versions that you create using AWS CodeBuild or AWS CodeCommit. For application versions built from a source bundle in Amazon S3, processing is optional.</p> <note> <p>The <code>Process</code> option validates Elastic Beanstalk configuration files. It doesn't validate your application's configuration files, like proxy server or Docker configuration.</p> </note>"""
    tags: NotRequired["aws_sdk_elastic_beanstalk.types.tags.Tags"]
    """<p>Specifies the tags applied to the application version.</p> <p>Elastic Beanstalk applies these tags only to the application version. Environments that use the application version don't inherit the tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateApplicationVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    pairs.append((f"{prefix}.VersionLabel", str(value["version_label"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "source_build_information" in value:
        import aws_sdk_elastic_beanstalk.types.source_build_information

        aws_sdk_elastic_beanstalk.types.source_build_information.serialize_query(
            value["source_build_information"], pairs, f"{prefix}.SourceBuildInformation"
        )
    if "source_bundle" in value:
        import aws_sdk_elastic_beanstalk.types.s3_location

        aws_sdk_elastic_beanstalk.types.s3_location.serialize_query(
            value["source_bundle"], pairs, f"{prefix}.SourceBundle"
        )
    if "build_configuration" in value:
        import aws_sdk_elastic_beanstalk.types.build_configuration

        aws_sdk_elastic_beanstalk.types.build_configuration.serialize_query(
            value["build_configuration"], pairs, f"{prefix}.BuildConfiguration"
        )
    if "auto_create_application" in value:
        pairs.append(
            (
                f"{prefix}.AutoCreateApplication",
                "true" if value["auto_create_application"] else "false",
            )
        )
    if "process" in value:
        pairs.append((f"{prefix}.Process", "true" if value["process"] else "false"))
    if "tags" in value:
        import aws_sdk_elastic_beanstalk.types.tags

        aws_sdk_elastic_beanstalk.types.tags.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateApplicationVersionMessage:
    out: CreateApplicationVersionMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError(
            "CreateApplicationVersionMessage.application_name required"
        )
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    else:
        raise DeserializationError(
            "CreateApplicationVersionMessage.version_label required"
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_source_build_information = el.find("SourceBuildInformation")
    if child_source_build_information is not None:
        import aws_sdk_elastic_beanstalk.types.source_build_information

        out["source_build_information"] = (
            aws_sdk_elastic_beanstalk.types.source_build_information.deserialize_query(
                child_source_build_information
            )
        )
    child_source_bundle = el.find("SourceBundle")
    if child_source_bundle is not None:
        import aws_sdk_elastic_beanstalk.types.s3_location

        out["source_bundle"] = (
            aws_sdk_elastic_beanstalk.types.s3_location.deserialize_query(
                child_source_bundle
            )
        )
    child_build_configuration = el.find("BuildConfiguration")
    if child_build_configuration is not None:
        import aws_sdk_elastic_beanstalk.types.build_configuration

        out["build_configuration"] = (
            aws_sdk_elastic_beanstalk.types.build_configuration.deserialize_query(
                child_build_configuration
            )
        )
    child_auto_create_application = el.find("AutoCreateApplication")
    if child_auto_create_application is not None:
        out["auto_create_application"] = (
            child_auto_create_application.text or ""
        ).lower() == "true"
    child_process = el.find("Process")
    if child_process is not None:
        out["process"] = (child_process.text or "").lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elastic_beanstalk.types.tags

        out["tags"] = aws_sdk_elastic_beanstalk.types.tags.deserialize_query(child_tags)
    return out
