"""Generated from Smithy shape ``com.amazonaws.rds#SupportedEngineLifecycleList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.supported_engine_lifecycle

SupportedEngineLifecycleList: TypeAlias = list[
    "capo_rds.types.supported_engine_lifecycle.SupportedEngineLifecycle"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedEngineLifecycleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.supported_engine_lifecycle

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.supported_engine_lifecycle.serialize_query(
            item, pairs, f"{prefix}.SupportedEngineLifecycle.{n}"
        )


def deserialize_query(el: Element) -> SupportedEngineLifecycleList:
    import capo_rds.types.supported_engine_lifecycle

    out: SupportedEngineLifecycleList = []
    for child in el.findall("SupportedEngineLifecycle"):
        out.append(capo_rds.types.supported_engine_lifecycle.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SupportedEngineLifecycleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.supported_engine_lifecycle

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.supported_engine_lifecycle.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SupportedEngineLifecycleList:
    import capo_rds.types.supported_engine_lifecycle

    out: SupportedEngineLifecycleList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.supported_engine_lifecycle.deserialize_query(child))
    return out
