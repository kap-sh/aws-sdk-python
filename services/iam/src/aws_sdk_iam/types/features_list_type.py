"""Generated from Smithy shape ``com.amazonaws.iam#FeaturesListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.feature_type

FeaturesListType: TypeAlias = list["aws_sdk_iam.types.feature_type.FeatureType"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FeaturesListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.feature_type

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.feature_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> FeaturesListType:
    import aws_sdk_iam.types.feature_type

    out: FeaturesListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.feature_type.deserialize_query(child))
    return out


def serialize_query_flat(
    value: FeaturesListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.feature_type

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.feature_type.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> FeaturesListType:
    import aws_sdk_iam.types.feature_type

    out: FeaturesListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.feature_type.deserialize_query(child))
    return out
