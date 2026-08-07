"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationVersionDescriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_version_description_list
    import capo_elastic_beanstalk.types.token


class ApplicationVersionDescriptionsMessage(TypedDict, closed=True):
    application_versions: NotRequired[
        "capo_elastic_beanstalk.types.application_version_description_list.ApplicationVersionDescriptionList"
    ]
    """<p>List of <code>ApplicationVersionDescription</code> objects sorted in order of creation.</p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.token.Token"]
    """<p>In a paginated request, the token that you can pass in a subsequent request to get the next response page.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationVersionDescriptionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_versions" in value:
        import capo_elastic_beanstalk.types.application_version_description_list

        capo_elastic_beanstalk.types.application_version_description_list.serialize_query(
            value["application_versions"], pairs, f"{key_prefix}ApplicationVersions"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ApplicationVersionDescriptionsMessage:
    out: ApplicationVersionDescriptionsMessage = {}  # type: ignore[typeddict-item]
    child_application_versions = el.find("ApplicationVersions")
    if child_application_versions is not None:
        import capo_elastic_beanstalk.types.application_version_description_list

        out["application_versions"] = (
            capo_elastic_beanstalk.types.application_version_description_list.deserialize_query(
                child_application_versions
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
