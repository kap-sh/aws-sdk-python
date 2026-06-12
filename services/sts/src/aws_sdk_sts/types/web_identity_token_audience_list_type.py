"""Generated from Smithy shape ``com.amazonaws.sts#webIdentityTokenAudienceListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.web_identity_token_audience_string_type

webIdentityTokenAudienceListType: TypeAlias = list[
    "aws_sdk_sts.types.web_identity_token_audience_string_type.webIdentityTokenAudienceStringType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: webIdentityTokenAudienceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> webIdentityTokenAudienceListType:
    out: webIdentityTokenAudienceListType = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: webIdentityTokenAudienceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(
    parent: Element, tag: str
) -> webIdentityTokenAudienceListType:
    out: webIdentityTokenAudienceListType = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
