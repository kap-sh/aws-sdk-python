"""Generated from Smithy shape ``com.amazonaws.elasticache#ParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.parameter

ParametersList: TypeAlias = list["capo_elasticache.types.parameter.Parameter"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ParametersList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.parameter

    for n, item in enumerate(value, 1):
        capo_elasticache.types.parameter.serialize_query(
            item, pairs, f"{prefix}.Parameter.{n}"
        )


def deserialize_query(el: Element) -> ParametersList:
    import capo_elasticache.types.parameter

    out: ParametersList = []
    for child in el.findall("Parameter"):
        out.append(capo_elasticache.types.parameter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ParametersList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.parameter

    for n, item in enumerate(value, 1):
        capo_elasticache.types.parameter.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ParametersList:
    import capo_elasticache.types.parameter

    out: ParametersList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.parameter.deserialize_query(child))
    return out
