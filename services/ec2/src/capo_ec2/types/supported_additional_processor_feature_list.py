"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedAdditionalProcessorFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.supported_additional_processor_feature

SupportedAdditionalProcessorFeatureList: TypeAlias = list[
    "capo_ec2.types.supported_additional_processor_feature.SupportedAdditionalProcessorFeature"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SupportedAdditionalProcessorFeatureList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.supported_additional_processor_feature

        capo_ec2.types.supported_additional_processor_feature.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SupportedAdditionalProcessorFeatureList:
    import capo_ec2.types.supported_additional_processor_feature

    out: SupportedAdditionalProcessorFeatureList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.supported_additional_processor_feature.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> SupportedAdditionalProcessorFeatureList:
    import capo_ec2.types.supported_additional_processor_feature

    out: SupportedAdditionalProcessorFeatureList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.supported_additional_processor_feature.deserialize_ec2_query(
                child
            )
        )
    return out
