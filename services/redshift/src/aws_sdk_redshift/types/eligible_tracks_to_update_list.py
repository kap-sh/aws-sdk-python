"""Generated from Smithy shape ``com.amazonaws.redshift#EligibleTracksToUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.update_target

EligibleTracksToUpdateList: TypeAlias = list[
    "aws_sdk_redshift.types.update_target.UpdateTarget"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EligibleTracksToUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.update_target

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.update_target.serialize_query(
            item, pairs, f"{prefix}.UpdateTarget.{n}"
        )


def deserialize_query(el: Element) -> EligibleTracksToUpdateList:
    import aws_sdk_redshift.types.update_target

    out: EligibleTracksToUpdateList = []
    for child in el.findall("UpdateTarget"):
        out.append(aws_sdk_redshift.types.update_target.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EligibleTracksToUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.update_target

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.update_target.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EligibleTracksToUpdateList:
    import aws_sdk_redshift.types.update_target

    out: EligibleTracksToUpdateList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.update_target.deserialize_query(child))
    return out
