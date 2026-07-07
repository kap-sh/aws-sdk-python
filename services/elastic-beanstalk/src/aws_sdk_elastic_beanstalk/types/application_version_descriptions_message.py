"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationVersionDescriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_version_description_list
    import aws_sdk_elastic_beanstalk.types.token


class ApplicationVersionDescriptionsMessage(TypedDict, closed=True):
    application_versions: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_version_description_list.ApplicationVersionDescriptionList"
    ]
    """<p>List of <code>ApplicationVersionDescription</code> objects sorted in order of creation.</p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.token.Token"]
    """<p>In a paginated request, the token that you can pass in a subsequent request to get the next response page.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationVersionDescriptionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "application_versions" in value:
        import aws_sdk_elastic_beanstalk.types.application_version_description_list

        aws_sdk_elastic_beanstalk.types.application_version_description_list.serialize_query(
            value["application_versions"], pairs, f"{prefix}.ApplicationVersions"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ApplicationVersionDescriptionsMessage:
    out: ApplicationVersionDescriptionsMessage = {}  # type: ignore[typeddict-item]
    child_application_versions = el.find("ApplicationVersions")
    if child_application_versions is not None:
        import aws_sdk_elastic_beanstalk.types.application_version_description_list

        out["application_versions"] = (
            aws_sdk_elastic_beanstalk.types.application_version_description_list.deserialize_query(
                child_application_versions
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
