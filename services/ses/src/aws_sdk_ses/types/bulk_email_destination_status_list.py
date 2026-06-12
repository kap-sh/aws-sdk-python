"""Generated from Smithy shape ``com.amazonaws.ses#BulkEmailDestinationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.bulk_email_destination_status

BulkEmailDestinationStatusList: TypeAlias = list[
    "aws_sdk_ses.types.bulk_email_destination_status.BulkEmailDestinationStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BulkEmailDestinationStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.bulk_email_destination_status

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.bulk_email_destination_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BulkEmailDestinationStatusList:
    import aws_sdk_ses.types.bulk_email_destination_status

    out: BulkEmailDestinationStatusList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_ses.types.bulk_email_destination_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: BulkEmailDestinationStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.bulk_email_destination_status

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.bulk_email_destination_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BulkEmailDestinationStatusList:
    import aws_sdk_ses.types.bulk_email_destination_status

    out: BulkEmailDestinationStatusList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ses.types.bulk_email_destination_status.deserialize_query(child)
        )
    return out
