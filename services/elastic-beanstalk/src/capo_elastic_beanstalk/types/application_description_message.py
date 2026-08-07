"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationDescriptionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_description


class ApplicationDescriptionMessage(TypedDict, closed=True):
    application: NotRequired[
        "capo_elastic_beanstalk.types.application_description.ApplicationDescription"
    ]
    """<p> The <a>ApplicationDescription</a> of the application. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationDescriptionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application" in value:
        import capo_elastic_beanstalk.types.application_description

        capo_elastic_beanstalk.types.application_description.serialize_query(
            value["application"], pairs, f"{key_prefix}Application"
        )


def deserialize_query(el: Element) -> ApplicationDescriptionMessage:
    out: ApplicationDescriptionMessage = {}  # type: ignore[typeddict-item]
    child_application = el.find("Application")
    if child_application is not None:
        import capo_elastic_beanstalk.types.application_description

        out["application"] = (
            capo_elastic_beanstalk.types.application_description.deserialize_query(
                child_application
            )
        )
    return out
