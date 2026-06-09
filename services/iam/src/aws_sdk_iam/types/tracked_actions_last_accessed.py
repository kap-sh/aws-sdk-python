"""Generated from Smithy shape ``com.amazonaws.iam#TrackedActionsLastAccessed``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.tracked_action_last_accessed

TrackedActionsLastAccessed: TypeAlias = list[
    "aws_sdk_iam.types.tracked_action_last_accessed.TrackedActionLastAccessed"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrackedActionsLastAccessed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.tracked_action_last_accessed

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.tracked_action_last_accessed.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TrackedActionsLastAccessed:
    import aws_sdk_iam.types.tracked_action_last_accessed

    out: TrackedActionsLastAccessed = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_iam.types.tracked_action_last_accessed.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TrackedActionsLastAccessed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.tracked_action_last_accessed

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.tracked_action_last_accessed.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TrackedActionsLastAccessed:
    import aws_sdk_iam.types.tracked_action_last_accessed

    out: TrackedActionsLastAccessed = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_iam.types.tracked_action_last_accessed.deserialize_query(child)
        )
    return out
