"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationDescriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_description


class ApplicationDescriptionMessage(TypedDict):
    application: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_description.ApplicationDescription"
    ]
    """<p> The <a>ApplicationDescription</a> of the application. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationDescriptionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application" in value:
        import aws_sdk_elastic_beanstalk.types.application_description

        aws_sdk_elastic_beanstalk.types.application_description.serialize_query(
            value["application"], pairs, f"{prefix}.Application"
        )


def deserialize_query(el: Element) -> ApplicationDescriptionMessage:
    out: ApplicationDescriptionMessage = {}  # type: ignore[typeddict-item]
    child_application = el.find("Application")
    if child_application is not None:
        import aws_sdk_elastic_beanstalk.types.application_description

        out["application"] = (
            aws_sdk_elastic_beanstalk.types.application_description.deserialize_query(
                child_application
            )
        )
    return out
