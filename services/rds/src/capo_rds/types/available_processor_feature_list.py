"""Generated from Smithy shape ``com.amazonaws.rds#AvailableProcessorFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.available_processor_feature

AvailableProcessorFeatureList: TypeAlias = list[
    "capo_rds.types.available_processor_feature.AvailableProcessorFeature"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableProcessorFeatureList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.available_processor_feature

    for n, item in enumerate(value, 1):
        capo_rds.types.available_processor_feature.serialize_query(
            item, pairs, f"{prefix}.AvailableProcessorFeature.{n}"
        )


def deserialize_query(el: Element) -> AvailableProcessorFeatureList:
    import capo_rds.types.available_processor_feature

    out: AvailableProcessorFeatureList = []
    for child in el.findall("AvailableProcessorFeature"):
        out.append(capo_rds.types.available_processor_feature.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AvailableProcessorFeatureList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.available_processor_feature

    for n, item in enumerate(value, 1):
        capo_rds.types.available_processor_feature.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AvailableProcessorFeatureList:
    import capo_rds.types.available_processor_feature

    out: AvailableProcessorFeatureList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.available_processor_feature.deserialize_query(child))
    return out
