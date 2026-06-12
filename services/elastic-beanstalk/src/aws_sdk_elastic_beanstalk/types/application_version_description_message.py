"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationVersionDescriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_version_description


class ApplicationVersionDescriptionMessage(TypedDict):
    application_version: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_version_description.ApplicationVersionDescription"
    ]
    """<p> The <a>ApplicationVersionDescription</a> of the application version. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationVersionDescriptionMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "application_version" in value:
        import aws_sdk_elastic_beanstalk.types.application_version_description

        aws_sdk_elastic_beanstalk.types.application_version_description.serialize_query(
            value["application_version"], pairs, f"{prefix}.ApplicationVersion"
        )


def deserialize_query(el: Element) -> ApplicationVersionDescriptionMessage:
    out: ApplicationVersionDescriptionMessage = {}  # type: ignore[typeddict-item]
    child_application_version = el.find("ApplicationVersion")
    if child_application_version is not None:
        import aws_sdk_elastic_beanstalk.types.application_version_description

        out["application_version"] = (
            aws_sdk_elastic_beanstalk.types.application_version_description.deserialize_query(
                child_application_version
            )
        )
    return out
