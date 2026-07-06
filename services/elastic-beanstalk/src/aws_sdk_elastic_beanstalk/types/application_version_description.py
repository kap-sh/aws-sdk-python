"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationVersionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.application_version_arn
    import aws_sdk_elastic_beanstalk.types.application_version_status
    import aws_sdk_elastic_beanstalk.types.creation_date
    import aws_sdk_elastic_beanstalk.types.description
    import aws_sdk_elastic_beanstalk.types.s3_location
    import aws_sdk_elastic_beanstalk.types.source_build_information
    import aws_sdk_elastic_beanstalk.types.string
    import aws_sdk_elastic_beanstalk.types.update_date
    import aws_sdk_elastic_beanstalk.types.version_label


class ApplicationVersionDescription(TypedDict, closed=True):
    application_version_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_version_arn.ApplicationVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the application version.</p>"""
    application_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application to which the application version belongs.</p>"""
    description: NotRequired["aws_sdk_elastic_beanstalk.types.description.Description"]
    """<p>The description of the application version.</p>"""
    version_label: NotRequired[
        "aws_sdk_elastic_beanstalk.types.version_label.VersionLabel"
    ]
    """<p>A unique identifier for the application version.</p>"""
    source_build_information: NotRequired[
        "aws_sdk_elastic_beanstalk.types.source_build_information.SourceBuildInformation"
    ]
    """<p>If the version's source code was retrieved from AWS CodeCommit, the location of the source code for the application version.</p>"""
    build_arn: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>Reference to the artifact from the AWS CodeBuild build.</p>"""
    source_bundle: NotRequired["aws_sdk_elastic_beanstalk.types.s3_location.S3Location"]
    """<p>The storage location of the application version's source bundle in Amazon S3.</p>"""
    date_created: NotRequired[
        "aws_sdk_elastic_beanstalk.types.creation_date.CreationDate"
    ]
    """<p>The creation date of the application version.</p>"""
    date_updated: NotRequired["aws_sdk_elastic_beanstalk.types.update_date.UpdateDate"]
    """<p>The last modified date of the application version.</p>"""
    status: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_version_status.ApplicationVersionStatus"
    ]
    """<p>The processing status of the application version. Reflects the state of the application version during its creation. Many of the values are only applicable if you specified <code>True</code> for the <code>Process</code> parameter of the <code>CreateApplicationVersion</code> action. The following list describes the possible values.</p> <ul> <li> <p> <code>Unprocessed</code> – Application version wasn't pre-processed or validated. Elastic Beanstalk will validate configuration files during deployment of the application version to an environment.</p> </li> <li> <p> <code>Processing</code> – Elastic Beanstalk is currently processing the application version.</p> </li> <li> <p> <code>Building</code> – Application version is currently undergoing an AWS CodeBuild build.</p> </li> <li> <p> <code>Processed</code> – Elastic Beanstalk was successfully pre-processed and validated.</p> </li> <li> <p> <code>Failed</code> – Either the AWS CodeBuild build failed or configuration files didn't pass validation. This application version isn't usable.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationVersionDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application_version_arn" in value:
        pairs.append(
            (f"{prefix}.ApplicationVersionArn", str(value["application_version_arn"]))
        )
    if "application_name" in value:
        pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "version_label" in value:
        pairs.append((f"{prefix}.VersionLabel", str(value["version_label"])))
    if "source_build_information" in value:
        import aws_sdk_elastic_beanstalk.types.source_build_information

        aws_sdk_elastic_beanstalk.types.source_build_information.serialize_query(
            value["source_build_information"], pairs, f"{prefix}.SourceBuildInformation"
        )
    if "build_arn" in value:
        pairs.append((f"{prefix}.BuildArn", str(value["build_arn"])))
    if "source_bundle" in value:
        import aws_sdk_elastic_beanstalk.types.s3_location

        aws_sdk_elastic_beanstalk.types.s3_location.serialize_query(
            value["source_bundle"], pairs, f"{prefix}.SourceBundle"
        )
    if "date_created" in value:
        import aws_sdk_elastic_beanstalk.types.creation_date

        aws_sdk_elastic_beanstalk.types.creation_date.serialize_query(
            value["date_created"], pairs, f"{prefix}.DateCreated"
        )
    if "date_updated" in value:
        import aws_sdk_elastic_beanstalk.types.update_date

        aws_sdk_elastic_beanstalk.types.update_date.serialize_query(
            value["date_updated"], pairs, f"{prefix}.DateUpdated"
        )
    if "status" in value:
        import aws_sdk_elastic_beanstalk.types.application_version_status

        aws_sdk_elastic_beanstalk.types.application_version_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_query(el: Element) -> ApplicationVersionDescription:
    out: ApplicationVersionDescription = {}  # type: ignore[typeddict-item]
    child_application_version_arn = el.find("ApplicationVersionArn")
    if child_application_version_arn is not None:
        out["application_version_arn"] = str(child_application_version_arn.text or "")
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    child_source_build_information = el.find("SourceBuildInformation")
    if child_source_build_information is not None:
        import aws_sdk_elastic_beanstalk.types.source_build_information

        out["source_build_information"] = (
            aws_sdk_elastic_beanstalk.types.source_build_information.deserialize_query(
                child_source_build_information
            )
        )
    child_build_arn = el.find("BuildArn")
    if child_build_arn is not None:
        out["build_arn"] = str(child_build_arn.text or "")
    child_source_bundle = el.find("SourceBundle")
    if child_source_bundle is not None:
        import aws_sdk_elastic_beanstalk.types.s3_location

        out["source_bundle"] = (
            aws_sdk_elastic_beanstalk.types.s3_location.deserialize_query(
                child_source_bundle
            )
        )
    child_date_created = el.find("DateCreated")
    if child_date_created is not None:
        import aws_sdk_elastic_beanstalk.types.creation_date

        out["date_created"] = (
            aws_sdk_elastic_beanstalk.types.creation_date.deserialize_query(
                child_date_created
            )
        )
    child_date_updated = el.find("DateUpdated")
    if child_date_updated is not None:
        import aws_sdk_elastic_beanstalk.types.update_date

        out["date_updated"] = (
            aws_sdk_elastic_beanstalk.types.update_date.deserialize_query(
                child_date_updated
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_elastic_beanstalk.types.application_version_status

        out["status"] = (
            aws_sdk_elastic_beanstalk.types.application_version_status.deserialize_query(
                child_status
            )
        )
    return out
