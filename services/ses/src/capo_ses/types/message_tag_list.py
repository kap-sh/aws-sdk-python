"""Generated from Smithy shape ``com.amazonaws.ses#MessageTagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.message_tag

MessageTagList: TypeAlias = list["capo_ses.types.message_tag.MessageTag"]


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.message_tag

    for n, item in enumerate(value, 1):
        capo_ses.types.message_tag.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> MessageTagList:
    import capo_ses.types.message_tag

    out: MessageTagList = []
    for child in el.findall("member"):
        out.append(capo_ses.types.message_tag.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MessageTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.message_tag

    for n, item in enumerate(value, 1):
        capo_ses.types.message_tag.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> MessageTagList:
    import capo_ses.types.message_tag

    out: MessageTagList = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.message_tag.deserialize_query(child))
    return out
