"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationDescriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_description_list


class ApplicationDescriptionsMessage(TypedDict, closed=True):
    applications: NotRequired[
        "capo_elastic_beanstalk.types.application_description_list.ApplicationDescriptionList"
    ]
    """<p>This parameter contains a list of <a>ApplicationDescription</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationDescriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "applications" in value:
        import capo_elastic_beanstalk.types.application_description_list

        capo_elastic_beanstalk.types.application_description_list.serialize_query(
            value["applications"], pairs, f"{prefix}.Applications"
        )


def deserialize_query(el: Element) -> ApplicationDescriptionsMessage:
    out: ApplicationDescriptionsMessage = {}  # type: ignore[typeddict-item]
    child_applications = el.find("Applications")
    if child_applications is not None:
        import capo_elastic_beanstalk.types.application_description_list

        out["applications"] = (
            capo_elastic_beanstalk.types.application_description_list.deserialize_query(
                child_applications
            )
        )
    return out
