"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedAdditionalProcessorFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.supported_additional_processor_feature

SupportedAdditionalProcessorFeatureList: TypeAlias = list[
    "aws_sdk_ec2.types.supported_additional_processor_feature.SupportedAdditionalProcessorFeature"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SupportedAdditionalProcessorFeatureList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.supported_additional_processor_feature

        aws_sdk_ec2.types.supported_additional_processor_feature.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> SupportedAdditionalProcessorFeatureList:
    import aws_sdk_ec2.types.supported_additional_processor_feature

    out: SupportedAdditionalProcessorFeatureList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.supported_additional_processor_feature.deserialize_ec2_query(
                child
            )
        )
    return out
