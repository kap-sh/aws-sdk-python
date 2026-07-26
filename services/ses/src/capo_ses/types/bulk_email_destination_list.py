"""Generated from Smithy shape ``com.amazonaws.ses#BulkEmailDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.bulk_email_destination

BulkEmailDestinationList: TypeAlias = list[
    "capo_ses.types.bulk_email_destination.BulkEmailDestination"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BulkEmailDestinationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.bulk_email_destination

    for n, item in enumerate(value, 1):
        capo_ses.types.bulk_email_destination.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BulkEmailDestinationList:
    import capo_ses.types.bulk_email_destination

    out: BulkEmailDestinationList = []
    for child in el.findall("member"):
        out.append(capo_ses.types.bulk_email_destination.deserialize_query(child))
    return out


def serialize_query_flat(
    value: BulkEmailDestinationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.bulk_email_destination

    for n, item in enumerate(value, 1):
        capo_ses.types.bulk_email_destination.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BulkEmailDestinationList:
    import capo_ses.types.bulk_email_destination

    out: BulkEmailDestinationList = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.bulk_email_destination.deserialize_query(child))
    return out
