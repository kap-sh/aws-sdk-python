"""Generated from Smithy shape ``com.amazonaws.rds#ProcessorFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.processor_feature

ProcessorFeatureList: TypeAlias = list[
    "capo_rds.types.processor_feature.ProcessorFeature"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ProcessorFeatureList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.processor_feature

    for n, item in enumerate(value, 1):
        capo_rds.types.processor_feature.serialize_query(
            item, pairs, f"{prefix}.ProcessorFeature.{n}"
        )


def deserialize_query(el: Element) -> ProcessorFeatureList:
    import capo_rds.types.processor_feature

    out: ProcessorFeatureList = []
    for child in el.findall("ProcessorFeature"):
        out.append(capo_rds.types.processor_feature.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ProcessorFeatureList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.processor_feature

    for n, item in enumerate(value, 1):
        capo_rds.types.processor_feature.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ProcessorFeatureList:
    import capo_rds.types.processor_feature

    out: ProcessorFeatureList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.processor_feature.deserialize_query(child))
    return out
