"""Generated from Smithy shape ``com.amazonaws.ses#BouncedRecipientInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.bounced_recipient_info

BouncedRecipientInfoList: TypeAlias = list[
    "aws_sdk_ses.types.bounced_recipient_info.BouncedRecipientInfo"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BouncedRecipientInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.bounced_recipient_info

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.bounced_recipient_info.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BouncedRecipientInfoList:
    import aws_sdk_ses.types.bounced_recipient_info

    out: BouncedRecipientInfoList = []
    for child in el.findall("member"):
        out.append(aws_sdk_ses.types.bounced_recipient_info.deserialize_query(child))
    return out


def serialize_query_flat(
    value: BouncedRecipientInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.bounced_recipient_info

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.bounced_recipient_info.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BouncedRecipientInfoList:
    import aws_sdk_ses.types.bounced_recipient_info

    out: BouncedRecipientInfoList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ses.types.bounced_recipient_info.deserialize_query(child))
    return out
