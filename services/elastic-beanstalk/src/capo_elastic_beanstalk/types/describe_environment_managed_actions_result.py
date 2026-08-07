"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEnvironmentManagedActionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.managed_actions


class DescribeEnvironmentManagedActionsResult(TypedDict, closed=True):
    managed_actions: NotRequired[
        "capo_elastic_beanstalk.types.managed_actions.ManagedActions"
    ]
    """<p>A list of upcoming and in-progress managed actions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEnvironmentManagedActionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "managed_actions" in value:
        import capo_elastic_beanstalk.types.managed_actions

        capo_elastic_beanstalk.types.managed_actions.serialize_query(
            value["managed_actions"], pairs, f"{key_prefix}ManagedActions"
        )


def deserialize_query(el: Element) -> DescribeEnvironmentManagedActionsResult:
    out: DescribeEnvironmentManagedActionsResult = {}  # type: ignore[typeddict-item]
    child_managed_actions = el.find("ManagedActions")
    if child_managed_actions is not None:
        import capo_elastic_beanstalk.types.managed_actions

        out["managed_actions"] = (
            capo_elastic_beanstalk.types.managed_actions.deserialize_query(
                child_managed_actions
            )
        )
    return out
