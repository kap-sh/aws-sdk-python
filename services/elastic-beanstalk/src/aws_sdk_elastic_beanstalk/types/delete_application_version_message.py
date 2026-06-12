"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeleteApplicationVersionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.delete_source_bundle
    import aws_sdk_elastic_beanstalk.types.version_label


class DeleteApplicationVersionMessage(TypedDict):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application to which the version belongs.</p>"""
    version_label: "aws_sdk_elastic_beanstalk.types.version_label.VersionLabel"
    """<p>The label of the version to delete.</p>"""
    delete_source_bundle: NotRequired[
        "aws_sdk_elastic_beanstalk.types.delete_source_bundle.DeleteSourceBundle"
    ]
    """<p>Set to <code>true</code> to delete the source bundle from your storage bucket. Otherwise, the application version is deleted only from Elastic Beanstalk and the source bundle remains in Amazon S3.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteApplicationVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    pairs.append((f"{prefix}.VersionLabel", str(value["version_label"])))
    if "delete_source_bundle" in value:
        pairs.append(
            (
                f"{prefix}.DeleteSourceBundle",
                "true" if value["delete_source_bundle"] else "false",
            )
        )


def deserialize_query(el: Element) -> DeleteApplicationVersionMessage:
    out: DeleteApplicationVersionMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError(
            "DeleteApplicationVersionMessage.application_name required"
        )
    child_version_label = el.find("VersionLabel")
    if child_version_label is not None:
        out["version_label"] = str(child_version_label.text or "")
    else:
        raise DeserializationError(
            "DeleteApplicationVersionMessage.version_label required"
        )
    child_delete_source_bundle = el.find("DeleteSourceBundle")
    if child_delete_source_bundle is not None:
        out["delete_source_bundle"] = (
            child_delete_source_bundle.text or ""
        ).lower() == "true"
    return out
