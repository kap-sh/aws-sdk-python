"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEnvironmentManagedActionHistoryResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.managed_action_history_items
    import aws_sdk_elastic_beanstalk.types.string


class DescribeEnvironmentManagedActionHistoryResult(TypedDict):
    managed_action_history_items: NotRequired[
        "aws_sdk_elastic_beanstalk.types.managed_action_history_items.ManagedActionHistoryItems"
    ]
    """<p>A list of completed and failed managed actions.</p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>A pagination token that you pass to <a>DescribeEnvironmentManagedActionHistory</a> to get the next page of results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEnvironmentManagedActionHistoryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "managed_action_history_items" in value:
        import aws_sdk_elastic_beanstalk.types.managed_action_history_items

        aws_sdk_elastic_beanstalk.types.managed_action_history_items.serialize_query(
            value["managed_action_history_items"],
            pairs,
            f"{prefix}.ManagedActionHistoryItems",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeEnvironmentManagedActionHistoryResult:
    out: DescribeEnvironmentManagedActionHistoryResult = {}  # type: ignore[typeddict-item]
    child_managed_action_history_items = el.find("ManagedActionHistoryItems")
    if child_managed_action_history_items is not None:
        import aws_sdk_elastic_beanstalk.types.managed_action_history_items

        out["managed_action_history_items"] = (
            aws_sdk_elastic_beanstalk.types.managed_action_history_items.deserialize_query(
                child_managed_action_history_items
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
