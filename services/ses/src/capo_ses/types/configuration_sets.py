"""Generated from Smithy shape ``com.amazonaws.ses#ConfigurationSets``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.configuration_set

ConfigurationSets: TypeAlias = list["capo_ses.types.configuration_set.ConfigurationSet"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSets, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.configuration_set

    for n, item in enumerate(value, 1):
        capo_ses.types.configuration_set.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ConfigurationSets:
    import capo_ses.types.configuration_set

    out: ConfigurationSets = []
    for child in el.findall("member"):
        out.append(capo_ses.types.configuration_set.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ConfigurationSets, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.configuration_set

    for n, item in enumerate(value, 1):
        capo_ses.types.configuration_set.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ConfigurationSets:
    import capo_ses.types.configuration_set

    out: ConfigurationSets = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.configuration_set.deserialize_query(child))
    return out
