"""Generated from Smithy shape ``com.amazonaws.sns#ListOfPlatformApplications``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.platform_application

ListOfPlatformApplications: TypeAlias = list[
    "capo_sns.types.platform_application.PlatformApplication"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOfPlatformApplications, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.platform_application

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.platform_application.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ListOfPlatformApplications:
    import capo_sns.types.platform_application

    out: ListOfPlatformApplications = []
    for child in el.findall("member"):
        out.append(capo_sns.types.platform_application.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ListOfPlatformApplications, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.platform_application

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.platform_application.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ListOfPlatformApplications:
    import capo_sns.types.platform_application

    out: ListOfPlatformApplications = []
    for child in parent.findall(tag):
        out.append(capo_sns.types.platform_application.deserialize_query(child))
    return out
