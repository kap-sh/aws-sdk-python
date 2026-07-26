"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEnvironmentManagedActionHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.managed_action_history_max_items
    import capo_elastic_beanstalk.types.string


class DescribeEnvironmentManagedActionHistoryRequest(TypedDict, closed=True):
    environment_id: NotRequired[
        "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The environment ID of the target environment.</p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the target environment.</p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The pagination token returned by a previous request.</p>"""
    max_items: NotRequired[
        "capo_elastic_beanstalk.types.managed_action_history_max_items.ManagedActionHistoryMaxItems"
    ]
    """<p>The maximum number of items to return for a single request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEnvironmentManagedActionHistoryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_items" in value:
        pairs.append((f"{prefix}.MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> DescribeEnvironmentManagedActionHistoryRequest:
    out: DescribeEnvironmentManagedActionHistoryRequest = {}  # type: ignore[typeddict-item]
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
