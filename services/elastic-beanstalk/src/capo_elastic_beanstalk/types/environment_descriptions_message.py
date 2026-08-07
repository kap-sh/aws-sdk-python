"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentDescriptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_descriptions_list
    import capo_elastic_beanstalk.types.token


class EnvironmentDescriptionsMessage(TypedDict, closed=True):
    environments: NotRequired[
        "capo_elastic_beanstalk.types.environment_descriptions_list.EnvironmentDescriptionsList"
    ]
    """<p> Returns an <a>EnvironmentDescription</a> list. </p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.token.Token"]
    """<p>In a paginated request, the token that you can pass in a subsequent request to get the next response page.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentDescriptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "environments" in value:
        import capo_elastic_beanstalk.types.environment_descriptions_list

        capo_elastic_beanstalk.types.environment_descriptions_list.serialize_query(
            value["environments"], pairs, f"{key_prefix}Environments"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> EnvironmentDescriptionsMessage:
    out: EnvironmentDescriptionsMessage = {}  # type: ignore[typeddict-item]
    child_environments = el.find("Environments")
    if child_environments is not None:
        import capo_elastic_beanstalk.types.environment_descriptions_list

        out["environments"] = (
            capo_elastic_beanstalk.types.environment_descriptions_list.deserialize_query(
                child_environments
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
