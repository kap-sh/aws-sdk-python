"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentDescriptionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_descriptions_list
    import aws_sdk_elastic_beanstalk.types.token


class EnvironmentDescriptionsMessage(TypedDict):
    environments: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_descriptions_list.EnvironmentDescriptionsList"
    ]
    """<p> Returns an <a>EnvironmentDescription</a> list. </p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.token.Token"]
    """<p>In a paginated request, the token that you can pass in a subsequent request to get the next response page.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentDescriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "environments" in value:
        import aws_sdk_elastic_beanstalk.types.environment_descriptions_list

        aws_sdk_elastic_beanstalk.types.environment_descriptions_list.serialize_query(
            value["environments"], pairs, f"{prefix}.Environments"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> EnvironmentDescriptionsMessage:
    out: EnvironmentDescriptionsMessage = {}  # type: ignore[typeddict-item]
    child_environments = el.find("Environments")
    if child_environments is not None:
        import aws_sdk_elastic_beanstalk.types.environment_descriptions_list

        out["environments"] = (
            aws_sdk_elastic_beanstalk.types.environment_descriptions_list.deserialize_query(
                child_environments
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
